from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Playlist-api is running"}

def test_get_all_songs_default_pagination():
    response = client.get("/songs")
    assert response.status_code == 200
    assert "total" in response.json()
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)

def test_get_song_by_title_valid():
    response = client.get("/songs/Believer")
    assert response.status_code == 200
    assert response.json()["title"].lower() == "believer"

def test_get_song_by_title_invalid():
    response = client.get("/songs/NonExistentTitle")
    assert response.status_code == 200
    assert "error" in response.json()

def test_rate_song_valid():
    response = client.post("/rate", json={"title": "Believer", "rating": 5})
    assert response.status_code == 200
    assert "message" in response.json()

def test_rate_song_invalid_rating():
    response = client.post("/rate", json={"title": "Believer", "rating": 6})
    assert response.status_code == 200
    assert response.json()["error"] == "Rating must be between 1 and 5"

def test_rate_song_invalid_title():
    response = client.post("/rate", json={"title": "Wrong Song", "rating": 3})
    assert response.status_code == 200
    assert "error" in response.json()
