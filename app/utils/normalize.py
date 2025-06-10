import json
import pandas as pd
from typing import List, Dict

def normalize_playlist_json(file_path: str) -> List[Dict]:
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    df = pd.DataFrame.from_dict(raw_data)

    # df.columns = [col.lower() for col in df.columns]
    df.reset_index(inplace=True)
    df.rename(columns={"index": "Index"}, inplace=True)

    cols = ['Index'] + [col for col in df.columns if col != 'Index']
    df = df[cols]

    df["star_rating"] = None

    return df.to_dict(orient="records")

def save_normalized_data_to_file(data: List[Dict], file_path: str = "data/normalized_output.json"):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
