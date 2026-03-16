import streamlit as st
from agents.supervisor_agent import ask

st.title("Assistente de Saúde Pública")

question = st.text_input("Faça uma pergunta")

if st.button("Perguntar"):

    response = ask(question)

    st.write(response)