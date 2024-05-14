import streamlit as st
from options import *
from pypdf import PdfReader 
from calculations import * 
from questions import questions

st.set_page_config(
    page_title="ISDE Regelhulp", 
    page_icon="🏠", 
    layout="centered", 
    initial_sidebar_state="collapsed", 
    menu_items={"Get help" : 'https://www.rvo.nl'}
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

/* Apply the font family to all elements */
* {
    font-family: 'Poppins', sans-serif;
}

/* Center align text in main container */
main .block-container {
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

/* Custom class for specifically aligned text if necessary */
.custom-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


def display_question(question):
    return st.write(question)

def main():
    if "page" not in st.session_state:
        st.session_state.page = 0

    def prevpage(): st.session_state.page -= 1
    def nextpage(): st.session_state.page += 1
    def restart(): st.session_state.page = 0

    for question in questions:
        if st.session_state.page == question.index:
            display_question(question)

    col1, col2 = st.columns([1,1])
    with col1:
        st.button("Vorige", on_click=prevpage, disabled=(st.session_state.page == 0))
    with col2:
        st.button("Volgende", on_click=nextpage, disabled=(st.session_state.page == 5))

    st.button("Opnieuw beginnen", on_click=restart, disabled=(st.session_state.page == 0))



if __name__ == '__main__':
        main()
