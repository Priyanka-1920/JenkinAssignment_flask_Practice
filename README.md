# Student Registration System

A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **Environment Variables:** Managed via `.env` file

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Priyanka-1920/JenkinAssignment_flask_Practice.git
cd JenkinAssignment_flask_Practice.git
```
**Create two branches:**
git checkout -b main
git push origin main

git checkout -b staging
git push origin staging

**Create GitHub Actions Workflow Directory**
.github/workflows/

Create a new workflow file:
.github/workflows/ci-cd.yml

Create the CI/CD Workflow File
ci-cd.yml

name: CI/CD Pipeline for Flask App

on: push: branches: - main - staging pull_request: branches: - main - staging release: types: [created]

**jobs:**

install-and-test: runs-on: ubuntu-latest

steps:
  - name: Checkout Code
    uses: actions/checkout@v3

  - name: Set up Python
    uses: actions/setup-python@v4
    with:
      python-version: '3.10'

  - name: Install Dependencies
    run: pip install -r requirements.txt

  - name: Run Tests
    run: |
      pip install pytest
      pytest
build: needs: install-and-test runs-on: ubuntu-latest if: success()

steps:
  - name: Checkout Code
    uses: actions/checkout@v3

  - name: Build Application
    run: |
      echo "Building application..."
      mkdir build
      cp -r app build/
      echo "Build complete!"
deploy-staging: needs: build runs-on: ubuntu-latest if: github.ref == 'refs/heads/staging'

steps:
  - name: Deploy to Staging
    run: |
      echo "Deploying to staging..."
      echo "Using secret key: ${{ secrets.STAGING_API_KEY }}"
      echo "Staging deployment done!"
deploy-production: needs: build runs-on: ubuntu-latest if: startsWith(github.ref, 'refs/tags/')

steps:
  - name: Deploy to Production
    run: |
      echo "Deploying to production..."
      echo "Using production key: ${{ secrets.PRODUCTION_API_KEY }}"
      echo "Production deployment done!"
**Add Environment Secrets**
Go to your repo: The workflow requires sensitive deployment credentials stored securely as GitHub Secrets.
**Click on Settings → Secrets and variables → Actions → New repository secret**

**Add the following secrets:**
STAGING_API_KEY Used for staging deployment
PRODUCTION_API_KEY Used for production deployment

These secrets are used in the workflow to authenticate deployment securely without exposing sensitive information in the code.

**GitHub Actions CI/CD Workflow**
This repository includes a GitHub Actions workflow to automate the Continuous Integration and Continuous Deployment (CI/CD) of the Flask application.

The workflow performs the following steps automatically:

Installs the necessary Python dependencies.
Runs the test suite using pytest to ensure code quality.
Builds/prepares the application if tests pass.
Deploys the application to the staging environment on push to the staging branch.
Deploys the application to the production environment when a release is tagged.
Branch Usage:
"staging" branch: This branch is used for deploying the application to the staging environment for testing before production release.
"main" branch or GitHub Releases: When a release tag is created (e.g., v1.0.0), the application is deployed to the production environment.
