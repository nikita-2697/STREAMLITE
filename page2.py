import streamlit as st
def showthis(val):
  st.write("second page",val)
  data = pd.read_csv("data.csv")
  return data;
