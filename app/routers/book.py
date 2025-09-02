from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.book_schema import BookCreate, BookRead
from app.core.db import get_session
from app.utilities.book_utility import create_book, get_book, list_books, remove_book

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=BookRead)
def create_book_endpoint(book: BookCreate, session: Session = Depends(get_session)):
    db_book = create_book(session, book)
    return db_book

@router.get("/", response_model=list[BookRead])
def read_books(session: Session = Depends(get_session)):
    books = list_books(session)
    return books

@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, session: Session = Depends(get_session)):
    book = get_book(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    success = remove_book(session, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book removed"}