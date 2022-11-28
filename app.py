import streamlit as st
import pandas as pd
import numpy as np

st.write("# My Subtraction Application")
st.write("Subtraction of two numbers...")

def user_input():
  a = st.number_input("Enter first number...")
  b = st.number_input("Enter second number...")
  data = {"A":a, "B":b}
  input = pd.DataFrame(data, index=[0])
  return input

#data = user_input();
x = st.number_input("Enter first number...")
y = st.number_input("Enter second number...")
z = x - y
st.write(x+" - "+y+" = "+z)
#st.write("###"+np.array2string(x[0])+" - "+np.array2string(y[0])+" = "+np.array2string(z[0]))  
