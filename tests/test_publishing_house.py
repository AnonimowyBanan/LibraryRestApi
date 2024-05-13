from .conftest import client


prefix = "/publishing-house/"
test_publishing_house_data = {"name": "Test Publishing House", "description": "Test Description"}
test_publishing_house_data_updated = {"name": "Updated test Publishing House", "description": "Updated test Description"}


def test_create(client):
    """
    Test the creation of a new publishing house.

    This test function sends a POST request to the "/publishing_house/" endpoint with a JSON payload containing
    the details of the new publishing house to be created. It then asserts that the HTTP status code of the response
    is 201, indicating that the publishing house was successfully created.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.post(prefix, json=test_publishing_house_data)

    assert response.status_code == 201


def test_get(client):
    """
    Test the retrieval of a publishing house.

    This test function sends a GET request to the "/publishing_house/" endpoint. It then asserts that the HTTP status code of
    the response is 200, indicating that the request was successful. It also checks that the 'name' and 'description'
    fields of the first publishing house in the response match the expected values, and that the response contains exactly one
    publishing house.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.get(prefix)

    assert response.status_code == 200
    assert response.json[0]['name'] == test_publishing_house_data['name']
    assert response.json[0]['description'] == test_publishing_house_data['description']
    assert len(response.json) == 1


def test_get_by_id(client):
    """
    Test the retrieval of a publishing house.

    This test function sends a GET request to the "/publishing_house/" endpoint. It then asserts that the HTTP status code of the response
    is 200, indicating that the request was successful. It also checks that the 'name' and 'description' fields of the first publishing house
    in the response match the expected values, and that the response contains exactly one publishing house.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.get(f"{prefix}1")

    assert response.status_code == 200
    assert response.json['name'] == test_publishing_house_data['name']
    assert response.json['description'] == test_publishing_house_data['description']


def test_update(client):
    """
    Test the update of a publishing house.

    This test function sends a PUT request to the "/publishing_house/" endpoint with a JSON payload containing
    the updated details of the publishing house. It then asserts that the HTTP status code of the response
    is 200, indicating that the publishing house was successfully updated.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.put(f"{prefix}1", json=test_publishing_house_data_updated)

    assert response.status_code == 201
    assert response.json['name'] == test_publishing_house_data_updated['name']
    assert response.json['description'] == test_publishing_house_data_updated['description']


def test_delete(client):
    """
    Test the deletion of a publishing house.

    This test function sends a DELETE request to the "/publishing_house/" endpoint. It then asserts that the HTTP status code of
    the response is 204, indicating that the publishing house was successfully deleted.

    Args:
        client (FlaskClient): The test client used to send requests to the application.

    """
    response = client.delete(f"{prefix}1")

    assert response.status_code == 204
