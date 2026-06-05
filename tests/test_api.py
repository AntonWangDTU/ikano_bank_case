from fastapi.testclient import TestClient
from ikano_case.api import app

client = TestClient(app)


"""Small tests of the api calls for the three functions """


def test_fibo():
    res = client.get("/fibo", params={"n": 5})
    assert res.status_code == 200
    assert res.json() == 5


def test_fibo_invalid():
    res = client.get("/fibo", params={"n": -1})
    assert res.status_code == 400


def test_fact():
    res = client.get("/fact", params={"n": 5})
    assert res.status_code == 200
    assert res.json() == 120


def test_fact_invalid():
    res = client.get("/fact", params={"n": -1})
    assert res.status_code == 400


# test invalid input into the loan endpoints
def test_loan():
    res = client.get("/loan", params={"P": 0, "r": 0.01, "n": 10})
    assert res.status_code == 400
