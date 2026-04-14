from pydantic import BaseModel


class TextRequest(BaseModel):
    """
    Request model for summarization
    """
    text: str