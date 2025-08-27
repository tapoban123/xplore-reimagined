from fastapi.testclient import TestClient

from ...main import app

client = TestClient(app=app)


def test_psychometric_question_generation():
    response = client.get("/ai/questions")
    assert response.status_code == 200
