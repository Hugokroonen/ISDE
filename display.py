import streamlit as st
from email_validator import validate_email, EmailNotValidError
import requests

import models

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
        f"<div style='text-align: center; font-size: 0.8rem;margin-bottom: 10px;'><i>Vraag {step_count} van {total_steps}</i></div>",
        unsafe_allow_html=True,
    )


def default_question_display(question: models.Question):
    display_title(question.question_text)
    display_description(question.help_text)
    
    col1, col2, col3 = st.columns([1,4,1])
    
    with col2:
        if question.type == models.QuestionType.NUMBER:
            question.answer = st.number_input(
                step=1,
                label=question.question_text, 
                label_visibility="hidden",
                value=question.answer or "min",
            )
        elif question.type == models.QuestionType.SELECTBOX:
            question.answer = st.selectbox(
                question.question_text, 
                question.options,
                label_visibility="hidden", 
                format_func= lambda option: option.text,
                help=question.help_text,
            )
        elif question.type == models.QuestionType.MULTISELECT:
            question.answer = st.multiselect(
                question.question_text, 
                question.options,
                label_visibility="hidden", 
                format_func= lambda option: option.text,
                help=question.help_text,
            )
        elif question.type == models.QuestionType.RADIO:
            question.answer = st.radio(
                question.question_text, 
                question.options,
                label_visibility="hidden", 
                format_func= lambda option: option.text,
                help=question.help_text,
            )
        elif question.type == models.QuestionType.BOOLEAN:
            question.answer = st.checkbox(
                question.question_text,
                label_visibility="hidden", 
                format_func= lambda option: option.text,
                help=question.help_text,
            )
        elif question.type == models.QuestionType.TEXT:
            question.answer = st.text_input(
                question.question_text,
                label_visibility="hidden", 
                help=question.help_text,
            )

def display_kick_off_request(question: models.Question):
    display_title(question.question_text)
    # display_description(question.help_text)

    st.info("Om zelf aan te vragen heb je toegang nodig tot DigiD. Is dit lastig? Kies dan één van de andere opties.")

    question.answer = st.radio(
        question.question_text, 
        question.options,
        label_visibility="hidden", 
        format_func= lambda option: option.text,
        help=question.help_text,
        args=(question,)
    )

    def next_callback():
        state = st.session_state
        question.info = None
        if question.answer.value == "self":
            state.question = models.Question.get_by_id("go_to_rvo", state.questions)

        if question.answer.value == "contact":
            state.question = models.Question.get_by_id("contact_me", state.questions)

        if question.answer.value == "request":
            state.question = models.Question.get_by_id("aanvragen", state.questions)

        state.previous_questions.append(question)

    st.button("Ga verder", type="primary", on_click=next_callback)


def display_email_field(question: models.Question):
    display_title(question.question_text)
    display_description(question.help_text)

    question.answer = st.text_input(
        question.question_text,
        placeholder="E-mail", 
        label_visibility="hidden", 
        help=question.help_text,
    )

    def next_callback():
        state = st.session_state
        question.error = None

        try:
            emailinfo = validate_email(question.answer)
            email = emailinfo.normalized
            state.result.email = email
            if question.id == "contact_me":
                state.result.intent = models.RequestIntent.SUPPORT
            elif question.id == "aanvragen":
                state.result.intent = models.RequestIntent.REQUEST

            requests.post("https://hooks.slack.com/services/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", json={'text': f"```{state.result.model_dump()}```"})
        except EmailNotValidError as e:
            question.error = "Ongeldig emailadres"
            return

        state.question = models.Question.get_by_id("bedankt_voor_je_aanvraag", state.questions)

        state.previous_questions.append(question)

    st.button("Versturen", type="primary", on_click=next_callback)

def display_subsidy_amount(question:models.Question):
    state = st.session_state

    display_title(question.question_text)
    col1, col2, col3 = st.columns([1,4,1])


    try:
        min_subsidy_formatted = f"€{state.result.min_subsidy_amount:,.0f}".replace(',', '.')
        max_subsidy_formatted = f"€{state.result.max_subsidy_amount:,.0f}".replace(',', '.')
        with col2:
            st.info(f"Je kunt tussen {min_subsidy_formatted} en {max_subsidy_formatted} ISDE ontvangen")
    except:
        with col2:
            st.info(f"Je kunt tussen €40,- en €12.675,- ISDE ontvangen")

    display_description(question.help_text)


