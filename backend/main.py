from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_root():
    return {
        "message": "Hello, World!"
    }