import pandas as pd

import streamlit as st

tab1, tab2 = st.tabs(["Cat", "Dog"])

with tab1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
  st.header("A tiger")
  st.image("https://static.streamlit.io/examples/tiger.jpg", width=200)
