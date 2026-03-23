import streamlit as st
from pages import input, result

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    
    st.session_state.page = "input"
    
if st.session_state.page == "input":
    
    input.show()
    
elif st.session_state.page == "output":
    
    result.show()