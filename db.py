import json

from schemas import Movie


def get_all_movies(json_file_path: str):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


def add_movie_to_json(movie: Movie, json_file_path: str):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    model_data = movie.dict()
    data.append(model_data)

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)


def get_movie_by_id(movie_id: int, json_file_path: str):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return None

    for record in data:
        if record.get('id') == movie_id:
            return record

    return None


def update_record_by_id(record_id: int, updated_data: dict, json_file_path: str):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return False

    updated = False
    for record in data:
        if record.get('id') == record_id:
            record.update(updated_data)
            updated = True
            break

    if updated:
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    else:
        return False