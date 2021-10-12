from main import app 
from fastapi.testclient import TestClient

client = TestClient(app)

def test1():
    response = client.get('/')
    assert response.status_code == 200
    