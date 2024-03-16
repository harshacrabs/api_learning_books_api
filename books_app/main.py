from fastapi import FastAPI
from . import schemas
from . import database


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the Books API"

@app.post("/book/")
def create_book(request: schemas.BookAuthorPayLoad):
    database.add_book(convert_into_book_db_model(request.book), convert_into_author_db_model(request.author))
    return ("New Book added" + " " + request.book.title + " " + str(request.book.number_of_pages) + " " 
    + "New author added" + " " + request.author.first_name + " " + request.author.last_name)


#The book schema from the request is not the same as the book schema in the database. The same goes for the author schema.
#We need to covert the requests schema into the database schema format

def convert_into_book_db_model(book: schemas.Book):
    return database.Book(title=book.title, number_of_pages=book.number_of_pages)


def convert_into_author_db_model(author: schemas.Author):
    return database.Author(first_name=author.first_name, last_name=author.last_name)
