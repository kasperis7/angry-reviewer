import streamlit as st
from processing import main

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.header("[AngryReviewer](https://www.angryreviewer.com/) Interactive Editor")
    text = st.text_area("Free academic style corrector for modern scientific writing. To get style suggestion for your abstracts, papers, theses, and applications, paste the text below.", height=600, placeholder="Input text here...")
    option = st.selectbox("option",('american', 'british'),label_visibility="collapsed")
    if st.button("Check"):
        result = main(text.split('\n'), english = option)
        for r in result:
            col2.write(r)
