from pydantic import BaseModel, field_validator
from typing import Callable, Optional, Union, Any, List
from enum import Enum
import streamlit as st

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
    MULTISELECT = "multiselect"
    NUMBER = "number"
    TEXT = "text"
    DISPLAY = "display"
    BOOLEAN = "boolean"
    RADIO = "radio"

class RequestIntent(str, Enum):
    SUPPORT = "support"
    REQUEST = "request"

class SubsidyResult(BaseModel):
    email: str | None = None
    postcode: str | None = None
    pc4: str | None = None
    home_owner: bool | None = None
    professional_installer: bool | None = None
    recently_applied: bool | None = None
    measures: list[Option] | None = None
    intent: RequestIntent | None = None

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
    show_previous_next: bool = True
    display_fun: Callable

    @classmethod
    def get_by_id(cls, id: str, questions: list['Question']):
        return next(filter(lambda question: question.id == id, questions))

    def display(self):
        self.display_fun(self)

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
        state.question = state.previous_questions[0]
        state.previous_questions = []

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
                self.error = "Helaas, je komt waarschijnlijk niet in aanmerking"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("nieuwbouw", state.questions)

        if self.id == "nieuwbouw":
            state.result.home_owner = self.answer.value
            if not state.result.home_owner:
                self.error = "Helaas, je komt waarschijnlijk niet in aanmerking"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("vorige_subsidie", state.questions)
    
        if self.id == "vorige_subsidie":
            state.result.home_owner = self.answer.value
            if not state.result.home_owner:
                self.error = "Helaas, je komt waarschijnlijk niet in aanmerking"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("installatiebedrijf", state.questions)

        if self.id == "datum":
            state.result.recently_applied = self.answer.value
            if not state.result.recently_applied:
                self.error = "Helaas, je komt waarschijnlijk niet in aanmerking"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("done", state.questions)


        if self.id == "installatiebedrijf":
            state.result.professional_installer = self.answer.value
            if not state.result.professional_installer:
                self.error = "Helaas, je komt waarschijnlijk niet in aanmerking"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("hoe_verder", state.questions)


        if self.id == "measure":
            state.result.measures = self.answer
            if len(state.result.measures) == 0:
                self.error = "Kies ten minste 1 maatregel"
                return
            else:
                self.clear_messages()
                state.question = Question.get_by_id("prep_done", state.questions)


        state.previous_questions.append(self)
