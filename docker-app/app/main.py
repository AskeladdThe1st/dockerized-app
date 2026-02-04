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
    required = ["DB_HOST","DB_PORT","DB_NAME","DB_USER","DB_PASSWORD"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        return {"error": f"Missing env vars: {missing}"}

    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    cur.close()
    conn.close()
    return {"db": "connected"}