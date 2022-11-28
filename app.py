import streamlit as st
import pandas as pd
import numpy as np

st.write("# My Subtraction Application")
st.write("Subtract two numbers...")

def user_input():
  a = st.number_input("Enter first number...")
  b = st.number_input("Enter second number...")
  data = {"A":a, "B":b}
  return pd.DataFrame(data)

data = user_input();
st.write(data.to_dict())
st.wite(data["A"]-data["B"])  
