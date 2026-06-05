# ikano_case

Solution to the Ikano Bank developer case. Exposes three mathematical functions (Fibonacci, Factorial, Loan repayment) via a FastAPI backend and a Streamlit frontend.

## Running with Docker (recommended)

```bash
docker compose up --build
```

| Service  | URL                        |
|----------|----------------------------|
| Frontend | http://localhost:8501      |
| API      | http://localhost:8000      |
| API docs | http://localhost:8000/docs |

## Running locally

**Prerequisites:** [uv](https://docs.astral.sh/uv/) and Python 3.12+

Install dependencies:

```bash
uv sync
```

Start the API:

```bash
uv run uvicorn ikano_case.api:app --reload
```

Start the frontend (in a separate terminal):

```bash
uv run streamlit run src/ikano_case/app.py
```

## API endpoints

| Endpoint | Parameters | Description |
|----------|-----------|-------------|
| `GET /fibo?n=10` | `n` (int ≥ 0) | n-th Fibonacci number |
| `GET /fact?n=5` | `n` (int ≥ 0) | n! factorial |
| `GET /loan?P=100000&r=0.005&n=360&M=0` | `P` principal, `r` monthly rate, `n` months, `M` repayment | Monthly loan repayment |

## CLI usage

The core functions can also be run directly from the command line:

```bash
# Fibonacci
uv run src/ikano_case/ikano_case.py fibo --n 10

# Factorial
uv run src/ikano_case/ikano_case.py fact --n 5

# Loan repayment (P=principal, r=monthly interest rate, n=months, M=monthly repayment)
uv run src/ikano_case/ikano_case.py loan --P 100000 --r 0.005 --n 360 --M 600
```

## Running tests

```bash
uv run pytest tests/
```

## Project structure

```
src/ikano_case/
├── ikano_case.py   # Core logic (fibo, fact, loan)
├── api.py          # FastAPI application
└── app.py          # Streamlit frontend
tests/
├── test_api.py
└── test_ikano_case.py
```

## Assumptions and Limitations

**Assumptions**
- The loan interest rate `r` is a monthly rate (e.g. `0.005` for 0.5% per month). No conversion from annual rates is performed.
- There are no caps on loan inputs — arbitrarily large principals, rates, or term lengths are accepted without warning.
- `n` for Fibonacci and Factorial must be a plain Python `int`; integer-like types (e.g. `numpy.int64`) are rejected.
- Loan repayments are always rounded to two decimal places, regardless of currency.

**Limitations**
- The factorial function is recursive with no iterative fallback, so very large inputs will hit Python's recursion limit.
- Zero-interest loans cannot be calculated; the loan function requires `r > 0`.
- All API parameters are passed as query strings, meaning sensitive financial values (principal, rate) appear in server logs.
