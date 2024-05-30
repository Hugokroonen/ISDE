import streamlit as st
from streamlit.components.v1 import html

def initialize_styling():
    st.markdown(
        """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Apply the font family to all elements */
    * {
        font-family: 'Poppins', sans-serif;
    }

    /* Center align text in main container */
    main .block-container, .stPageLink  {
        text-align: center; 
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    /* Override Streamlit's default alignment for markdown text, including headers */
    .markdown-text-container, .markdown-text-container h1, .markdown-text-container h2, .markdown-text-container h3 {
        text-align: center !important;
    }

    /* Center images and buttons */
    .stImage, .stButton>button {
        margin: 0 auto !important;
        display: block;
    }

    .styles_streamlitAppContainer__w82h8.styles_embed__UIgBb {
        border: none;
    }
    
    /* Custom class for specifically aligned text if necessary */
    .custom-text {
        text-align: center;
    }

    .stRadio label {
        margin-bottom: 10px;
    }

    div.st-cc.st-bn.st-ar.st-cd.st-ce.st-cf {visibility: hidden;}
    div.st-cc.st-bn.st-ar.st-cd.st-ce.st-cf:before {content: "Kies opties"; visibility: visible;}
    </style>
    """,
        unsafe_allow_html=True,
    )