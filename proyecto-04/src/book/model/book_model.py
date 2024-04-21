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
                    "titulo": "Ejemplo",
                    "autor": [
                        {
                            "id": uuid1(),
                            "nombre": "Ejemplo",
                            "fecha_nacimiento": "01-01-2001",
                        }
                    ],
                    "categoria": "ejemplo",
                    "year": 2024,
                }
            ]
        }
    }
