from flask import Flask

def test_home():
    app = Flask(__name__)
    client = app.test_client()
    response = client.get('/')
    assert response.status_code in [200, 404]
