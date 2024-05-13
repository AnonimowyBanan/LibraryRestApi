from .conftest import client


test_author_data = {"first_name": "Test Author Name", "last_name": "Test Author Last Name",
                    "biography": "Test Biography"}
test_author_data_updated = {"first_name": "Test Author Name Updated", "last_name": "Test Author Last Name Updated",
                            "biography": "Test Biography Updated"}


def test_create(client):
    """
    Test the creation of a new author.

    This test function sends a POST request to the "/author/" endpoint with a JSON payload containing
    the details of the new author to be created. It then asserts that the HTTP status code of the response
    is 201, indicating that the author was successfully created.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.post("/author/", json=test_author_data)

    assert response.status_code == 201


def test_get(client):
    """
    Test the retrieval of all authors.

    This test function sends a GET request to the "/author/" endpoint to retrieve all authors.
    It then asserts that the HTTP status code of the response is 200 and that the response data
    is a list of dictionaries, each containing the details of an author.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.get("/author/")

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert all(isinstance(author, dict) for author in response.json)


def test_get_by_id(client):
    """
    Test the retrieval of a single author by ID.

    This test function sends a GET request to the "/author/<author_id>" endpoint to retrieve a single author
    by their ID. It then asserts that the HTTP status code of the response is 200 and that the response data
    is a dictionary containing the details of the author.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.get("/author/1")

    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json["first_name"] == test_author_data["first_name"]
    assert response.json["last_name"] == test_author_data["last_name"]
    assert response.json["biography"] == test_author_data["biography"]


def test_update(client):
    """
    Test the update of an existing author.

    This test function sends a PUT request to the "/author/<author_id>" endpoint with a JSON payload containing
    the updated details of an author. It then asserts that the HTTP status code of the response is 201, indicating
    that the author was successfully updated.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.put("/author/1", json=test_author_data_updated)

    assert response.status_code == 201
    assert response.json["first_name"] == test_author_data_updated["first_name"]
    assert response.json["last_name"] == test_author_data_updated["last_name"]
    assert response.json["biography"] == test_author_data_updated["biography"]


def test_delete(client):
    """
    Test the deletion of an author.

    This test function sends a DELETE request to the "/author/<author_id>" endpoint to delete an author by their ID.
    It then asserts that the HTTP status code of the response is 200 and that the response data is a dictionary
    containing the details of the deleted author.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.delete("/author/1")

    assert response.status_code == 200
    assert response.json["first_name"] == "Test Author Name Updated"
    assert response.json["last_name"] == "Test Author Last Name Updated"
    assert response.json["biography"] == "Test Biography Updated"
