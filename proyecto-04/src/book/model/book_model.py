"""Book model"""

from typing import Optional
from uuid import uuid1
from pydantic import BaseModel, Field

from src.author.model.author import Author


class BookModel(BaseModel):
    """Book properties"""

    id: Optional[str] = str(uuid1())
    title: str = Field(min_length=5, max_length=20)
    authors: list[Author] = Field()
    category: str = Field(min_length=5, max_length=10)
    release_date: int = Field(le=2024)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": uuid1(),
                    "title": "Ejemplo",
                    "authors": [
                        {
                            "id": uuid1(),
                            "fullname": "Ejemplo",
                            "date_birth": "01-01-2001",
                        }
                    ],
                    "category": "ejemplo",
                    "release_date": 2024,
                }
            ]
        }
    }
