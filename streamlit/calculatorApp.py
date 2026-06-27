import streamlit as st

st.title("A simple calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operation = st.selectbox("Choose operation", ["select method", "Add", "Subtract", "Multiply", "Divide"])

if st.button("calculate"):
    if operation == "select method":
        result = "select the method first"
    elif operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "cannot divide by zero"
    st.success(f"result: {result}")


