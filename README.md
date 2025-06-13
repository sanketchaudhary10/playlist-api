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

```plaintext
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
    ├── .gitignore
    ├── pytest.ini
    └── README.md
```

## Setup Instructions (Local)

## 1. Cloning the Repository
```bash
git clone https://github.com/sanketchaudhary10/playlist-api.git
cd playlist-api
```

## 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate # On Windows
pip install -r requirements.txt
```

## 3. Run the app
```bash
uvicorn app.main:app --reload
```

## 4. Accessing the app at: http://localhost:8000/docs

## Built by Sanket Chaudhary
