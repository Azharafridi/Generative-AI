import streamlit as st
import pandas as pd
import numpy as np


## title of the application:
st.title("Hello Streamlit")

## display a  simple text

st.write("this is a simple text")

## create a simple dataframe

df = pd.DataFrame({
    'first column': [1,2, 3, 4],
    'second column': [10, 20, 30, 40]    
})

## Display the dataframe
st.write("this is a simple dataframe")
st.write(df)

## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)