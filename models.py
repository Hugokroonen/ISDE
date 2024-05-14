from pydantic import BaseModel
from typing import Optional, Union, Any, List

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
        return False

class Question(BaseModel):
    index: int