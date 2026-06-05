"""ikano_case."""

from ikano_case.ikano_case import fibo, fact, loan
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi import HTTPException


app = FastAPI()


# GET endpoint for the the fibonacci
@app.get("/fibo")
async def read_fibo(n: int = 5):
    try:
        return fibo(n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET endpoint for the the factorial function
@app.get("/fact")
async def read_fact(n: int = 5):
    try:
        return fact(n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET endpoint for the the fibo
@app.get("/loan")
async def read_loan(P: float, r: float, n: int):
    try:
        return loan(P, r, n)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
