import pytest
from ikano_case.ikano_case import fibo, fact, loan


# Tests for fibonacci function
def test_fibo():
    assert fibo(0) == 0
    assert fibo(5) == 5
    assert fibo(10) == 55


def test_fibo_negative_input():
    with pytest.raises(ValueError):
        fact(-1)


# Tests for factorial function
def test_fact():
    assert fact(0) == 1
    assert fact(5) == 120
    assert fact(10) == 3628800


def test_fact_negative_input():
    with pytest.raises(ValueError):
        fact(-1)


# Tests for the loan function
def test_loan():
    assert loan(1000, 0.01, 10) == pytest.approx(105.55, rel=1e-2)


# Test invalid inputs for the loan function
def test_loan_negative_input():
    with pytest.raises(ValueError):
        loan(-1000, 0.01, 12)
    with pytest.raises(ValueError):
        loan(1000, -0.01, 12)
    with pytest.raises(ValueError):
        loan(1000, 0.01, -12)
