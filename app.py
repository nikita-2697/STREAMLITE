import streamlit as st
import pandas as pd
st.write("HIII")
header = st.container()
with header:
  st.title("Hii welcome")
  data = st.read_csv("data.csv")
  st.write(data.head)
