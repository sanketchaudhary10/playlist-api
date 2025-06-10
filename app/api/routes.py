from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Playlist-api is running"}