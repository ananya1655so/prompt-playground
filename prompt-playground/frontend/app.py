import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Prompt Playground", layout="wide")
st.title("🧪 Prompt Playground")

st.write("Compare and improve AI prompts side-by-side")

col1, col2 = st.columns(2)

with col1:
    prompt1 = st.text_area("Prompt Version 1", height=200)

with col2:
    prompt2 = st.text_area("Prompt Version 2", height=200)

user_input = st.text_input("Input for both prompts")

if st.button("Run Comparison"):
    if not prompt1 or not prompt2:
        st.warning("Please enter both prompts.")
    else:
        response = requests.post(
            f"{BACKEND_URL}/run",
            json={
                "prompts": [prompt1, prompt2],
                "user_input": user_input
            }
        ).json()

        for i, output in enumerate(response["outputs"]):
            st.subheader(f"Output {i+1}")
            st.code(output)
            st.json(response["scores"][i])

if st.button("Improve Prompt 1"):
    if not prompt1:
        st.warning("Enter Prompt Version 1 first.")
    else:
        response = requests.post(
            f"{BACKEND_URL}/improve",
            json={
                "prompts": [prompt1],
                "user_input": ""
            }
        ).json()

        st.subheader("Improved Prompt")
        st.code(response["improved_prompt"])

