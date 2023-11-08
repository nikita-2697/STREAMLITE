import streamlit as st
import pandas as pd
import page2 as p2
import plotly.express as px
import streamlit as st
# from prophet import Prophet
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
</style> """, unsafe_allow_html=True)
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

st.line_chart(data, x='Date', y='Count',color=None)
