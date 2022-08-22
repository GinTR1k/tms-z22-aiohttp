import pytest
import requests

from some_code import get_pets


@pytest.fixture()
def pet_store_response():
    response = requests.Response()
    response._content = b'[]'
    response.status_code = 200
    return response


@pytest.fixture()
def pet_store_error_response(pet_store_response):
    pet_store_response.status_code = 500
    return pet_store_response


@pytest.fixture()
def requests_get(mocker):
    return mocker.patch('some_code.requests.get')


@pytest.fixture()
def pending_status():
    return 'pending'


@pytest.fixture()
def available_status():
    return 'available'


def test_pet_store(pet_store_response, available_status, requests_get):
    requests_get.return_value = pet_store_response
    assert get_pets(available_status) == []
    requests_get.assert_called_with(f'https://petstore.swagger.io/v2/pet/findByStatus?status={available_status}')


def test_pet_store_error(pet_store_error_response, pending_status, requests_get):
    requests_get.return_value = pet_store_error_response
    with pytest.raises(Exception):
        get_pets(pending_status)
    requests_get.assert_called_with(f'https://petstore.swagger.io/v2/pet/findByStatus?status={pending_status}')
