from pydantic import BaseModel
from typing import List

class PromptRequest(BaseModel):
    prompts: List[str]
    user_input: str
