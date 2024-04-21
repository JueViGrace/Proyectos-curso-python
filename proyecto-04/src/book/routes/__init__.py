"""Books routes"""

from json import dump, load
from operator import itemgetter
from uuid import uuid1
from fastapi import APIRouter, Path, Query, status
from fastapi.responses import JSONResponse

from src.book.model.book_model import BookModel
from src.db import dirname
from src.app.utils.logger import logger

books_router = APIRouter()


@books_router.get("/")
def get_books():
    """Get all books"""
    with open(f"{dirname}/db.json", "r", encoding="utf-8") as db:
        data = load(db)

        return JSONResponse(content=data["books"], status_code=200)


@books_router.get("/{book_id}")
def get_book_by_id(book_id: str = Path(min_length=10)):
    """Get one book by id"""
    with open(f"{dirname}/db.json", "r", encoding="utf-8") as db:
        data = load(db)

        for book in data["books"]:
            if book["id"] == book_id:
                return book

        return JSONResponse(
            content={"message": "Book not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@books_router.get("/find/")
def get_book_by_title(title: str = Query(min_length=5, max_length=20)):
    """Get book by title"""
    with open(f"{dirname}/db.json", "r", encoding="utf-8") as db:
        data = load(db)

        for book in data["books"]:
            if book["title"].lower().startswith(title.lower()):
                return book

        return JSONResponse(
            content={"message": "Book not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@books_router.post("/create")
def create_book(body: BookModel):
    """Create book"""
    id, title, category, release_date, authors = itemgetter(
        "id", "title", "category", "release_date", "authors"
    )(body.model_dump())

    valid_authors = []

    with open(f"{dirname}/db.json", "r", encoding="utf-8") as db:
        data = load(db)

        for author in authors:
            valid_authors = [
                db_author
                for db_author in data["authors"]
                if author["id"] == db_author["id"]
            ]
            logger.debug(author)

    if len(valid_authors) == 0:
        return JSONResponse(
            content={"message": "One or more authors is not valid"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    new_book = {
        "id": uuid1(),
        "title": title,
        "category": category,
        "release_date": release_date,
        "authors": authors,
    }

    data["books"].append(new_book)

    with open(f"{dirname}/db.json", "w", encoding="utf-8") as db:
        dump(data, db, indent=2)

    return JSONResponse(content={"message": "Book created successfully"})


@books_router.put("/update/{id}")
def update_book(id: str, body: BookModel):
    """Update book"""


@books_router.delete("/delete/{id}")
def delete_book(id: str = Path(min_length=10)):
    """Delete book"""
