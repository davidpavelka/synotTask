import requests

def test_cat_fact_api():
    response = requests.get("https://catfact.ninja/fact")
    assert response.status_code == 200
    data = response.json()
    assert "fact" in data and isinstance(data["fact"], str)
    assert "length" in data and isinstance(data["length"], int)
