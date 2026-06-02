"""ikano_case."""

from ikano_case.ikano_case import fibo, fact, loan
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pathlib import Path



app = FastAPI()


FUNCTIONS = {
    "fibo": fibo,
    "fact": fact,
    "loan": loan,
}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/fibo")
async def read_item(n: int = 5):
    return fibo(n)

@app.get("/fact")
async def read_item(n: int = 5):
    return fact(n)


@app.get("/loan")
async def read_item(P: float, r: float, n: int, M: int):
    return loan(P, r, n, M)

