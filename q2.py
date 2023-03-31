import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

st.set_page_config(layout="wide")

BASE_URL = "http://localhost:8000"

def process_file(file):
    df = pd.read_excel(file, sheet_name=0)
    return df

st.title('File Upload Interface')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = process_file(uploaded_file)
    process_button = st.button("Process text")
    df = df.to_json()
    inputs = {"file": df}
    
    if process_button:
        result = requests.post(url = f"{BASE_URL}/process", json = inputs)
        st.subheader(f"{result.text}")