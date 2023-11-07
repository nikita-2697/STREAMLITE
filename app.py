import streamlit as st
import pandas as pd
import page2 as p2
import plotly.express as px
import streamlit as st
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

st.line_chart(data, x=data['Date'].head(), y=data['Count'].head(),color=None)
