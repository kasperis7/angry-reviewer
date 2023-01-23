import streamlit as st
from processing import main

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.header("[AngryReviewer](https://www.angryreviewer.com/) Interactive Editor")
    text = st.text_area("Text to be analyzed", height=600, placeholder="Input text here...")
    if st.button("Analyze"):
        result = main(text.split('\n'))
        for r in result:
            col2.write(r)
