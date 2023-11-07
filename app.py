import streamlit as st
import pandas as pd
import page2 as p2
st.write("HIII")
header = st.container()
with header:
  st.title("Hii welcome")
  data = pd.read_csv("data.csv")
  st.write(data.head())
  abc= data['14.14'].head()
  val = st.selectbox("AccountID", abc)
  p2.showthis(val)
