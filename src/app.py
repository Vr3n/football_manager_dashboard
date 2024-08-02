from fastapi import FastAPI

from database import db_lifespan


app: FastAPI = FastAPI(lifespan=db_lifespan)


@app.get("/", tags=["root"])
async def read_root():
    return {
        "message": "welcome to the application!"
    }
