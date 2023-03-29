import streamlit as st
import pandas as pd
import numpy as np

# st.set_page_config(layout="wide")

st.title('File Upload Interface')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    pass