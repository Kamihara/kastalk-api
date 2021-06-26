from typing import Optional

from pydantic import BaseModel


class NormalLang(BaseModel):
    word: str
