from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Playlist-api is running"}

@router.get("/songs")
def get_all_songs(request: Request):
    return request.app.state.normalized_data

