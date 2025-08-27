from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app=app)


def test_otp_route():
    signUp_res = client.post("/student/auth/send-sign-up-otp", params={"receiver_email": "raytapoban@gmail.com"})
    assert signUp_res.status_code == 200

