from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, FastAPI with Docker!'}

def test_read_item():
    response = client.get('/items/42?q=test')
    assert response.status_code == 200
    assert response.json() == {'item_id': 42, 'q': 'test'}

def test_read_item_without_query():
    response = client.get('/items/42')
    assert response.status_code == 200
    assert response.json() == {'item_id': 42, 'q': None}
