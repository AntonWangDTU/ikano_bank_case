import streamlit as st
import requests
import os

# API_URL = "http://localhost:8000"
API_URL = os.getenv(
    "API_URL", "http://localhost:8000"
)  # uses the env set by docker compose
st.title("Ikano Bank Case")

# input for fubo
st.header("Fibonacci")
fibo_n = st.number_input("n", min_value=0, step=1, key="fibo_n")
if st.button("Calculate fibonacci"):
    res = requests.get(f"{API_URL}/fibo", params={"n": int(fibo_n)})
    if res.status_code == 200:
        st.write(res.text)
    else:
        st.error(res.json()["detail"])


st.divider()

# Input for fact
st.header("Factorial")
fact_n = st.number_input("n", min_value=0, step=1, key="fact_n")
if st.button("Calculate factorial"):
    res = requests.get(f"{API_URL}/fact", params={"n": int(fact_n)})
    if res.status_code == 200:
        st.write(res.text)
    else:
        st.error(res.json()["detail"])

st.divider()

#
# Input fields
st.header("Loan")
P = st.number_input("Principal (P)", min_value=0.0, key="loan_P")
r = st.number_input(
    "Monthly interest rate (r)", min_value=0.001, format="%.4f", key="loan_r"
)
n = st.number_input("Number of months (n)", min_value=1, step=1, key="loan_n")
# if you click
if st.button("Calculate your monthly repayment"):
    res = requests.get(f"{API_URL}/loan", params={"P": P, "r": r, "n": int(n)})
    if res.status_code == 200:
        st.write(res.text)
    else:
        st.error(res.json()["detail"])

