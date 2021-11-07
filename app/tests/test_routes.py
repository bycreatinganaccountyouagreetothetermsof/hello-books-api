def test_get_all_books_with_no_records(client):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_book_with_no_records(client):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None


def test_get_all_books(client, two_saved_books):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {"id": 1, "title": "Ocean Book", "description": "watr 4evr"},
        {"id": 2, "title": "Mountain Book", "description": "i luv 2 climb rocks"},
    ]


def test_get_one_book(client, two_saved_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"id": 1, "title": "Ocean Book", "description": "watr 4evr"}


def test_post_one_book(client):
    pluto = {
        "title": "pluto",
        "description": "the bravest book",
    }
    response = client.post("/books", json=pluto)
    assert response.status_code == 201
