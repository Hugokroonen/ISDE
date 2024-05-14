import streamlit as st

def display_title(text: str):
    st.markdown(
        f"<h6 style='color: #00007E; text-align: center;'>{text}</h6>",
        unsafe_allow_html=True,
    )
    
def display_description(text: str):
    st.markdown(
        f"<div style='text-align: center;font-size: 0.8rem;'>{text}</div>",
        unsafe_allow_html=True,
    )