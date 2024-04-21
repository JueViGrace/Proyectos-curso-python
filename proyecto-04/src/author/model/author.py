"""Author model"""

from typing import Optional
from uuid import uuid1
from pydantic import BaseModel, Field


class Author(BaseModel):
    """Author properties"""

    id: Optional[str]
    fullname: str = Field(min_length=5, max_length=45)
    date_birth: str = Field(
        regexp="\b(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19\d\d|20\d\d)\b"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": uuid1(),
                    "fullname": "Ejemplo",
                    "date_birth": "01-01-2001",
                }
            ]
        }
    }
