import streamlit as st
import requests
import os

#API_URL = "http://localhost:8000"
API_URL = os.getenv("API_URL", "http://localhost:8000")  # uses the env st by docker compose
st.title("Ikano Bank Case")

# --- Fibonacci ---
st.header("Fibonacci")
fibo_n = st.number_input("n", min_value=0, step=1, key="fibo_n")
if st.button("Calculate fibo"):
    res = requests.get(f"{API_URL}/fibo", params={"n": int(fibo_n)})
    st.write(res.text)

st.divider()

# --- Factorial ---
st.header("Factorial")
fact_n = st.number_input("n", min_value=0, step=1, key="fact_n")
if st.button("Calculate fact"):
    res = requests.get(f"{API_URL}/fact", params={"n": int(fact_n)})
    st.write(res.text)

st.divider()

# --- Loan ---
st.header("Loan")
P = st.number_input("Principal (P)", min_value=0.0, key="loan_P")
r = st.number_input("Monthly interest rate (r)", min_value=0.001, format="%.4f", key="loan_r")
n = st.number_input("Number of months (n)", min_value=1, step=1, key="loan_n")
M = st.number_input("Monthly repayment", min_value=1, step=1, key="loan_M")
if st.button("Calculate loan"):
    res = requests.get(f"{API_URL}/loan", params={"P": P, "r": r, "n": int(n), "M": M})
    st.write(res.text)