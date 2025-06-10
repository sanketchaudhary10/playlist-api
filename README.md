# Playlist-API

## Overview
A FastAPI-based web service to normalize and serve song playlist data from a JSON file.

**Features**:
- Normalize playlist JSON into a tabular structure.

- `GET /songs`  
  Returns all songs processed in the json response.

- `GET /songs/{title}`  
  Lookup any song by title

- `POST /rate`  
  Rate songs (1–5 stars).

- Support offset-based pagination (`offset` & `limit`)

- Saves the data to a JSON file for storage.

## Tech Stack:
- Python
- FastAPI
- Uvicorn

## Project Structure:

playlist-api/
├── app/
│ ├── main.py
│ ├── api/routes.py
│ └── utils/normalize.py
├── data/
│ ├── playlist.json
│ └── normalized_output.json
├── tests/
│ └── test_routes.py
├── requirements.txt
├── pytest.ini
└── README.md