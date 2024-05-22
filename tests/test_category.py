from .conftest import client

url = "/category/"

test_category_data = {"name": "Test Category", "description": "Test Description"}
test_category_data_updated = {"name": "Updated test Category", "description": "Updated test Description"}


def test_create(client):
    """
    Test the creation of a new category.

    This test function sends a POST request to the "/category/" endpoint with a JSON payload containing
    the details of the new category to be created. It then asserts that the HTTP status code of the response
    is 201, indicating that the category was successfully created.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.post(url, json=test_category_data)

    assert response.status_code == 201


def test_get(client):
    """
    Test the retrieval of a category.

    This test function sends a GET request to the "/category/" endpoint. It then asserts that the HTTP status code of
    the response is 200, indicating that the request was successful. It also checks that the 'name' and 'description'
    fields of the first category in the response match the expected values, and that the response contains exactly one
    category.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.get(url)

    assert response.status_code == 200
    assert response.json[0]['name'] == test_category_data['name']
    assert response.json[0]['description'] == test_category_data['description']
    assert len(response.json) == 1


def test_get_by_id(client):
    """
    Test the retrieval of a category.

    This test function sends a GET request to the "/category/" endpoint. It then asserts that the HTTP status code of the response
    is 200, indicating that the request was successful. It also checks that the 'name' and 'description' fields of the first category
    in the response match the expected values, and that the response contains exactly one category.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.get(f"{url}1")

    assert response.status_code == 200
    assert response.json['name'] == test_category_data['name']
    assert response.json['description'] == test_category_data['description']


def test_update(client):
    """
    Test the update of a category.

    This test function sends a PUT request to the "/category/1" endpoint with a JSON payload containing
    the updated details of the category. It then asserts that the HTTP status code of the response
    is 201, indicating that the update was successful. It also checks that the 'name' and 'description'
    fields of the category in the response match the updated values.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.put(f"{url}1", json=test_category_data_updated)

    assert response.status_code == 201
    assert response.json['name'] == test_category_data_updated['name']
    assert response.json['description'] == test_category_data_updated['description']


def test_delete(client):
    """
    Test the update of a category.

    This test function sends a PUT request to the "/category/1" endpoint with a JSON payload containing
    the updated details of the category. It then asserts that the HTTP status code of the response
    is 201, indicating that the update was successful. It also checks that the 'name' and 'description'
    fields of the category in the response match the updated values.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.delete(f"{url}1")

    assert response.status_code == 200
