"""Authors routes"""

from json import load
from fastapi import APIRouter, Path, status
from fastapi.responses import JSONResponse

from src.db import dirname

authors_router = APIRouter()


@authors_router.get('/')
def get_authors():
    """Get all authors"""
    with open(f"{dirname}/db.json", "r", encoding="utf-8") as db:
        data = load(db)

        return JSONResponse(content=data["authors"], status_code=200)


@authors_router.get("/{author_id}")
def get_authors_by_id(author_id: str = Path(min_length=10)):
    """Get all authors"""
    with open(f"{dirname}/db.json", "r", encoding="utf-8") as db:
        data = load(db)

        for author in data["authors"]:
            if author["id"] == author_id:
                return JSONResponse(content=author, status_code=status.HTTP_200_OK)

        return JSONResponse(
            content={"message": "Author not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
