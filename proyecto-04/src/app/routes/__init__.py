'''App routes'''

from fastapi import APIRouter
from src.author.routes import authors_router
from src.book.routes import books_router

app_router = APIRouter()

app_router.include_router(books_router, prefix='/books', tags=['books'])
app_router.include_router(authors_router, prefix='/authors', tags=['authors'])
