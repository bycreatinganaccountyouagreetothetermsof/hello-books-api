from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world", __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books")


@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body


@hello_world_bp.route("/hello-world/json", methods=["GET"])
def json_hello_world():
    my_ugly_response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"],
    }
    return my_ugly_response_body


@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"],
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body


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
