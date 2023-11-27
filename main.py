import json

from fastapi import FastAPI, HTTPException

from db import get_movie_by_id, add_movie_to_json, update_record_by_id, get_all_movies


app = FastAPI()


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    movie = get_movie_by_id(movie_id=movie_id, json_file_path='example.json')
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.get("/movies/")
def list_movies():
    movies = get_all_movies(json_file_path='example.json')
    return movies


@app.post("/movies/")
def create_movie(movie: Movie):
    add_movie_to_json(movie=movie, json_file_path='example.json')
    return movie


@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, updated_data: Movie):
    update_record_by_id(
        record_id=movie_id,
        updated_data=updated_data.dict(),
        json_file_path='example.json'
    )
    return {'status': 'ok'}