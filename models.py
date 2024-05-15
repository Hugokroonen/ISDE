from pydantic import BaseModel
from typing import Callable, Optional, Union, Any, List
from enum import Enum
import streamlit as st
from display import *

# Base Option class
class Option(BaseModel):
    text: str
    value: Optional[Union[str, int]] = None
    help: Optional[str] = None
    icon_path: Optional[str] = None

    def __eq__(self, other: Any):
        try:
            return self.text == other.text and self.value == other.value
        except (ValueError, AttributeError):
            return False

class QuestionType(str, Enum):
    SLIDER = "slider"
    SELECTBOX = "selectbox"
    NUMBER = "number"
    TEXT = "text"
    DISPLAY = "display"
    BOOLEAN = "boolean"


class SubsidyResult(BaseModel):
    postcode: str | None = None
    pc4: str | None = None
    home_owner: bool | None = None


class Question(BaseModel):
    id: str
    index: int = -1
    question_text: str
    help_text: str
    type: QuestionType
    options: list[Option] | None = None
    answer: Any | None = None
    error: str | None = None
    success: str | None = None
    info: str | None = None

    @classmethod
    def get_by_id(cls, id: str, questions: list['Question']):
        return next(filter(lambda question: question.id == id, questions))

    def display(self):

        display_title(self.question_text)
        display_description(self.help_text)
        
        if self.type == QuestionType.NUMBER:
            self.answer = st.number_input(
                step=1,
                label=self.question_text, 
                label_visibility="hidden",
                value=self.answer or "min",
            )
        elif self.type == QuestionType.SELECTBOX:
            self.answer = st.selectbox(
                self.question_text, 
                self.options,
                label_visibility="hidden", 
                format_func= lambda option: option.text,
                help=self.help_text,
            )
        elif self.type == QuestionType.BOOLEAN:
            self.answer = st.checkbox(
                self.question_text,
                label_visibility="hidden", 
                format_func= lambda option: option.text,
                help=self.help_text,
            )

    def clear_messages(self):
        self.error = None
        self.success = None
        self.info = None

    def on_previous_callback(self, state):
        self.clear_messages()

        state.question = state.previous_questions[-1]
        state.previous_questions = state.previous_questions[:-1]

    def on_restart_callback(self, state):
        self.clear_messages()

        state.result = SubsidyResult()
        state.previous_questions = []
        state.question = Question.get_by_id("koopwoning", state.questions)

    def previous_disabled(self, state):
        return len(state.previous_questions) == 0
    
    def next_disabled(self, state):
        return self.id == "done"

    def restart_disabled(self, state):
        return len(state.previous_questions) == 0

    def on_next_callback(self, state):
        
        if self.id == "postcode":
            if self.answer < 1000 or self.answer > 9999:
                self.error = "Ongeldige postcode"
                return
            else:
                self.clear_messages()
                state.result.postcode = self.answer
                state.question = Question.get_by_id("done", state.questions)
        
        if self.id == "koopwoning":
            state.result.home_owner = self.answer.value
            if not state.result.home_owner:
                self.error = "Helaas, je komt niet in aanmerking"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("done", state.questions)


        state.previous_questions.append(self)
