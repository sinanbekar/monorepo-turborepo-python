from fastapi.testclient import TestClient

from hello_fastapi.main import app


client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
