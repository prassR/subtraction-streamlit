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

data = user_input();
x = data["A"]
y = data["B"]
z = x - y
st.write(z.values())  
