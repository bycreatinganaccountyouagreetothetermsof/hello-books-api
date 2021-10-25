from flask.signals import request_tearing_down
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

book_bp = Blueprint("book", __name__, url_prefix="/books")


@book_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        return jsonify(
            [
                {"id": book.id, "title": book.title, "description": book.description}
                for book in Book.query.all()
            ]
        )
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(
            title=request_body["title"], description=request_body["description"]
        )
        db.session.add(new_book)
        db.session.commit()
        return make_response(f"Book {new_book.title} successfully created", 201)


@book_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return make_response(f"Book {book_id} not found", 404)
    if request.method == "GET":
        return {"id": book.id, "title": book.title, "description": book.description}
    elif request.method == "PUT":
        request_body = request.get_json()
        book.title = request_body["title"]
        book.description = request_body["description"]
        db.session.commit()
        return make_response(f"Book {book_id} successfully updated")
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book {book_id} successfully deleted")
