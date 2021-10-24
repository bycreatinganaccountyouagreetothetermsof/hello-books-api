from flask.signals import request_tearing_down
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

book_bp = Blueprint("book", __name__, url_prefix="/books")


@book_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"], description=request_body["description"]
    )
    db.session.add(new_book)
    db.session.commit()
    return make_response(f"Book {new_book.title} successfully created", 201)


# @books_bp.route("", methods=["GET"])
# def handle_books():
#    books_response = []
#    for book in books:
#        books_response.append(
#            {"id": book.id, "title": book.title, "description": book.description}
#        )
#    return jsonify(books_response)
#
#
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#    book_id = int(book_id)
#    for book in books:
#        if book.id == book_id:
#            return {"id": book.id, "title": book.title, "description": book.description}
