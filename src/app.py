from os import environ as env
import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from src.logger import init_logging
from src.todos_manager.manager import TodosDBManager


# Load configurations

HOST = env.get('APP_HOST', "0.0.0.0")
PORT = int(env.get('APP_PORT', 8080))
LOG_LEVEL = env.get('LOGLEVEL', 'INFO').upper()
DB_URL = env.get('DB_URL', 'mongodb://localhost:27017').upper()
todos_db_manager = TodosDBManager(DB_URL)
app = FastAPI()
logger = init_logging(LOG_LEVEL)


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT)
