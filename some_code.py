from typing import Union

import requests


def division(a: Union[int, float], b: Union[int, float]) -> float:
    if b == 0:
        return 0.0
    if not isinstance(a, (int, float)):
        raise TypeError('a is not an int')
    if not isinstance(b, (int, float)):
        raise TypeError('b is not an int')

    return a / b

# TDD - Test Driven Development


def get_pets(status: str) -> list[dict]:
    response = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}')
    if response.status_code != 200:
        raise Exception('Error')
    return response.json()
