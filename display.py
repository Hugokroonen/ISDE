import streamlit as st

def display_title(text: str):
    st.markdown(
        f"<h5 style='color: #00007E; text-align: center;'>{text}</h5>",
        unsafe_allow_html=True,
    )
    
def display_description(text: str):
    st.markdown(
        f"<div style='text-align: center;'>{text}</div>",
        unsafe_allow_html=True,
    )

def display_steps(step_count: int, total_steps: int):
    st.markdown(
        f"<div style='text-align: center; font-size: 0.8rem;margin-bottom: 10px;'><i>Stap {step_count} van {total_steps}</i></div>",
        unsafe_allow_html=True,
    )