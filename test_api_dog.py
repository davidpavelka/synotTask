import requests

def test_dog_api_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://")
    assert data["message"].endswith((".jpg", ".jpeg", ".png"))
