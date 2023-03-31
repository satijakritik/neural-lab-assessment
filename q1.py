from datetime import time
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

st.title('Function Column Visualizer')

FILE_PATH = "stats_full_stack_dev.csv"

@st.cache_data
def loadData(nrows):
    data = pd.read_csv(FILE_PATH, nrows = nrows) 
    return data

def findUniqueValues(df):
    return df['Function'].unique()

st.text_input("Number of rows to visualize", key="num_of_rows")

num_of_rows = st.session_state.num_of_rows
data = None
error_text_state = st.text('')

if num_of_rows.isdigit():
    num_of_rows = int(num_of_rows)
    data_load_state = st.text('Loading data...')
    data = loadData(num_of_rows)
    data_load_state.text("Done!")
    st.subheader('Data')
    st.write(data)
else:
    error_text_state.text('Enter a valid integer!')
    

if data is not None:
    unique_vals = findUniqueValues(data)
    
    num_of_columns = st.selectbox('Number of columns in grid layout', (1, 2, 3), index = 1)
    num_of_columns = int(num_of_columns)
    
    columns = st.columns(num_of_columns)
    
    for i, function_name in enumerate(unique_vals):
        temp = data[ data['Function'] == function_name]
        temp = temp[['time_stamp','Time']]
        
        for j, column in enumerate(columns):
            if i % num_of_columns == j:
                fig = px.line(temp.sort_values("time_stamp"), x="time_stamp", y="Time", title=function_name)
                column.plotly_chart(fig, use_container_width=True)