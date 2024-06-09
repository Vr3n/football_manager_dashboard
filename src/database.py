from contextlib import asynccontextmanager
from logging import info
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings


@asynccontextmanager
async def db_lifespan(app: FastAPI):

    # startup
    app.mongodb_client = AsyncIOMotorClient(settings.mongod_uri)
    app.database = app.mongodb_client.get_default_database()

    ping_response = await app.database.command("ping")

    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster!")
    else:
        info("Connected to database cluster.")

    yield

    # shut down.
    app.mongodb_client.close()
