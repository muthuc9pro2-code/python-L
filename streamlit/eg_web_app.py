import streamlit as st

st.title("First streamlit App")
st.header("Welcome to my demo App")
st.write("This is a simple app built with streamlit!")

name  = st.text_input("what is your name?")
if name:
    st.success(f"Hello {name}")

age = st.slider("select your age", 1, 100, 25)
st.write("You selected:", age)