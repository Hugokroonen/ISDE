import streamlit as st
from models import SubsidyResult
from options import *
from pypdf import PdfReader
from calculations import *
from questions import questions

st.set_page_config(
    page_title="ISDE Regelhulp",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": "https://www.rvo.nl"},
)

st.markdown(
    """
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

.stAlert {
    font-size: 0.8rem;
}
</style>
""",
    unsafe_allow_html=True,
)

def main():
    if "questions" not in st.session_state:
        st.session_state.questions = questions
        st.session_state.question = questions[0]
    if "result" not in st.session_state:
        st.session_state.result = SubsidyResult()
    

    question = st.session_state.question

    prevpage = lambda: question.on_previous_callback(st.session_state)
    nextpage = lambda: question.on_next_callback(st.session_state)
    restart = lambda: question.on_restart_callback(st.session_state)

    question.display()
    if question.error:
        st.error(question.error)
    if question.success:
        st.success(question.success)
    if question.info:
        st.info(question.info)


    col1, col2 = st.columns([1, 1])
    with col1:
        st.button(
            "Vorige", 
            on_click=prevpage, 
            disabled=question.previous_disabled(st.session_state)
        )
    with col2:
        st.button(
            "Volgende", 
            on_click=nextpage, 
            disabled=question.next_disabled(st.session_state),
            type="primary"
        )

    st.button(
        "Opnieuw beginnen", 
        on_click=restart, 
        disabled=question.restart_disabled(st.session_state)
    )

    st.code(st.session_state.result)

if __name__ == "__main__":
    main()
