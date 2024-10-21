from pydantic import BaseModel


class Language(BaseModel):
    language: str
    code: str
