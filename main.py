from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def get_user_by_id(user_id: int):
    return user_id % 2  # ej


@app.get("/users/{user_id}")
async def users(user_id: int):
    return get_user_by_id(user_id=user_id)


class AvatarColor(
    str, Enum
):  # Importante que sea str, Enum y no Enum, str, porque primero quiero que AvatarColor.red sea un string
    red = "red"
    blue = "blue"
    green = "green"
