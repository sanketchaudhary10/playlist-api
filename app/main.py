from fastapi import FastAPI
from app.api.routes import router as api_router
from app.utils.normalize import normalize_playlist_json

app = FastAPI(title="Playlist Normalizer")

normalized_data = normalize_playlist_json("data/playlist.json")
app.state.normalized_data = normalized_data

app.include_router(api_router)
