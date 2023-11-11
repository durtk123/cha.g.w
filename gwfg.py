import streamlit as st
import pandas as pd
st.metric(label="온도", value="10℃", delta="1.2℃")
st.metric(label="삼성전자", value="61,000원", delta="-1,200 원")

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228원", delta="-12.00원")

import streamlit as st

tab1, tab2 = st.tabs(["Cat", "Dog"])

with tab1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
