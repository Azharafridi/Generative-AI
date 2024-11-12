import pandas as pd
import streamlit as st


st.title("stream text input")

name = st.text_input("Enter you name: ")

## create a slider
age = st.slider("select your age: ",0, 100, 25)

st.write(f"You are {age} years old" )

# choice selectbox
options = ["Python", "Java", "JavaScript"]
choice = st.selectbox("choose your favorite language: ",options)
st.write(f"You selected {choice}.")


if name:
    st.write(f"Hello,  {name}")  
data = {
    "Name" : ['azhar', "emmi afridi", "afridi", "Noor"],
    "Age" : [23, 20, 35, 32],
    "city" : ["Houston", "new York", "chicago", "new York"]
    
    
}

# create uplaod button
uploaded_file = st.file_uploader("upload a CSV file", type="csv") 
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df) 