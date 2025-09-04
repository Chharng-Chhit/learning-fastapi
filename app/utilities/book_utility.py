from typing import List, Dict, Optional
from sqlalchemy.orm import Session

from app.models.model import Book
from app.schemas.book_schema import BookCreate


class BookUtility:
    def __init__(self):
        self.books: List[Dict] = []

    def add_book(db: Session, book: BookCreate) -> Dict:
        book = {
            "title": book.title,
            "desc": book.desc
        }
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def get_book(self, book_id: int) -> Optional[Dict]:
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def list_books(self) -> List[Dict]:
        return self.books

    def remove_book(self, book_id: int) -> bool:
        for i, book in enumerate(self.books):
            if book["id"] == book_id:
                del self.books[i]
                return True
        return False


def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def list_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def remove_book(db: Session, book_id: int) -> bool:
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return True
    return False