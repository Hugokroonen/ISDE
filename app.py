import streamlit as st
from models import Question, SubsidyResult
from options import *
from pypdf import PdfReader
from calculations import *
from questions import voorwaarden
from display import display_steps
from utils import initialize_styling

st.set_page_config(
    page_title="ISDE Regelhulp",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={"Get help": "https://energieklus.nl/bewoners"},
)

initialize_styling()

def main():
    st.session_state.questions = voorwaarden
    if "previous_questions" not in st.session_state:
        st.session_state.previous_questions = []

    if not(len(st.session_state.previous_questions) > 0 and st.session_state.previous_questions[-1] in st.session_state.questions):
        st.session_state.question = Question.get_by_id("koopwoning", st.session_state.questions)
        st.session_state.previous_questions = []

    if "result" not in st.session_state:
        st.session_state.result = SubsidyResult()

    question = st.session_state.question

    prevpage = lambda: question.on_previous_callback(st.session_state)
    nextpage = lambda: question.on_next_callback(st.session_state)
    restart = lambda: question.on_restart_callback(st.session_state)

    display_steps(len(st.session_state.previous_questions) + 1, 6)

    question.display()
    
    if question.error:
        st.error(question.error)
    if question.success:
        st.success(question.success)
    if question.info:
        st.info(question.info)

    if question.show_previous_next:
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col2:
            st.button(
                "Vorige", 
                on_click=prevpage, 
                disabled=question.previous_disabled(st.session_state)
            )
        with col3:
            st.button(
                "Volgende", 
                on_click=nextpage, 
                disabled=question.next_disabled(st.session_state),
                type="primary"
            )

    if question.id != "hoe_verder":
        st.markdown("""---""")
    if question.id == "hoe_verder":
        st.markdown(" ")

    st.page_link(
        "pages/1_Voorbereiding.py",
        label=":pencil: :blue[Stap 2. Aanvraag voorbereiden?]"
    )
    st.page_link(
        "pages/2_Aanvragen.py",
        label=":rocket: :blue[Stap 3. Direct aanvragen]"
    )

    st.button(
        "Opnieuw beginnen", 
        on_click=restart, 
        disabled=question.restart_disabled(st.session_state)
    )

    # st.code(st.session_state.result)

if __name__ == "__main__":
    main()
