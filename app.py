import streamlit as st
import pandas as pd
import page2 as p2
st.write("HIII")
header = st.container()
with header:
  st.title("Hii welcome")
  data = pd.read_csv("data.csv")
  st.write(data['7036745'].head())
  p2.showthis()
