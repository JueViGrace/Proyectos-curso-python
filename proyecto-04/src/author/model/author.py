"""Author model"""

from typing import Optional
from uuid import uuid1
from pydantic import UUID1, BaseModel, Field


class Author(BaseModel):
    """Author properties"""

    id: Optional[UUID1] = uuid1()
    nombre: str = Field(min_length=5, max_length=45)
    fecha_nacimiento: str = Field(pattern="DD-MM-YYYY")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": uuid1(),
                    "nombre": "Ejemplo",
                    "fecha_nacimiento": '01-01-2001',
                }
            ]
        }
    }
