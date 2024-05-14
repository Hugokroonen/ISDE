from pydantic import BaseModel
from typing import Optional, Union, Any, List

class QuestionType(BaseModel):
    SLIDER = "slider"
    SELECTBOX = "selectbox"
    NUMBER = "number_input"
    TEXT = "text_input"

class Option(BaseModel):
    text: str
    value: Any

class Question(BaseModel):
    id: str
    question_text: str
    help_text: str | None = None
    question_type: QuestionType
    options: list[Answer] | None = None

class Answer(BaseModel):
    question_id: str
    value: Any


    condition_not_met = Answer(
    question_id="postcode",
    value = "Jouw gemeente doet helaas nog niet mee. Dat betekent dat je nog geen gebruik kunt maken van de gratis subsidiehulp"
)