import streamlit as st
import pandas as pd
import page2 as p2
import matplotlib.pyplot as plt
import seaborn as sns
# from prophet import Prophet
st.write("HIII")
header = st.container()
with header:
  st.title("Hii welcome")
  data = pd.read_csv("data.csv")
  st.write(data.head())
  abc= data['Date'].head()
  val = st.selectbox("AccountID", abc)
  p2.showthis(val)
# m=Prophet()
# st.set_page_config(page_title = "")
