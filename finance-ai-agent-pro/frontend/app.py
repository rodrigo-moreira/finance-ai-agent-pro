import streamlit as st
import requests

st.title("💼 Finance AI Agent")

risk = st.slider("Risco (1-10)", 1, 10)
amount = st.number_input("Valor (R$)", min_value=0.0)
goal = st.text_input("Objetivo financeiro")

if st.button("Analisar"):
    response = requests.post(
        "http://localhost:8000/analyze",
        json={
            "risk": risk,
            "amount": amount,
            "goal": goal
        }
    )

    data = response.json()

    st.subheader("Resultado")
    st.write(data)
