from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["status"] == "operational"

def test_status_tool():
    response = client.get("/status/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data["data"]

def test_excuse_tool():
    response = client.get("/excuse/")
    assert response.status_code == 200
    data = response.json()
    assert "excuse" in data["data"]

def test_decision_coin():
    response = client.get("/decision/coin")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["result"] in ["Heads", "Tails"]

def test_decision_magic8():
    response = client.get("/decision/magic-8-ball")
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data["data"]
