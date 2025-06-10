from typing import Optional
from fastapi import APIRouter, Request, Query

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Playlist-api is running"}

@router.get("/songs")
def get_all_songs(request: Request):
    return request.app.state.normalized_data

@router.get("/songs/{title}")
def get_all_songs(request: Request, title: str):
    data = request.app.state.normalized_data
    res = []

    for song in data:
        if song['title'].lower() == title.lower():
            res.append(song)
    
    if res:
        return res[0]

    return {"Error": "Song not found! Please enter the correct name again."}


# @router.get("/songs{title}")
# def get_all_songs(request: Request, title: Optional[str] = Query(None, description="Title of the song")):
#     data = request.app.state.normalized_data
#     res = []

#     if title:
#         for song in data:
#             if song['title'].lower() == title.lower():
#                 res.append(song)
#                 return res

#     return data

