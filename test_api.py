
from fastapi.testclient import TestClient
from api import app
client = TestClient(app)
def test_predict_valid():
    response = client.post("/predict", json={"year":2023, "month":6})
    assert response.status_code == 200
    assert "prediction" in response.json()
def test_predict_invalid():
    response = client.post("/predict", json={"year":"abc", "month":6})
    assert response.status_code == 422
