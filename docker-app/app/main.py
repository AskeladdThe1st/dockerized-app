from fastapi import FastAPI
from typing import Union
import os
import psycopg2

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/db")
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    cur.close()
    conn.close()
    return {"db": "connected"}