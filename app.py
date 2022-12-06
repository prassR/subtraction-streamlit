import streamlit as st

st.write("Subtraction Application")
st.write("Subtraction of two numbers...")


x = st.number_input("Enter first number...")
y = st.number_input("Enter second number...")
z = x - y
st.write(str(x)+" - "+str(y)+" = "+str(z))
