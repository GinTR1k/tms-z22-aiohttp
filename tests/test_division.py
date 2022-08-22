from pathlib import Path

import pytest

from some_code import division


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1, 1, 1),
        (4, 2, 2),
        (45, 5, 9),
        (.5e2, 2, 25),
        (1, 0, 0),
        (0, 1, 0),
    ]
)
def test_division(a, b, expected):
    result = division(a, b)
    assert result == expected
    assert type(result) == float


@pytest.mark.parametrize(
    'a, b, expected_exception',
    [
        ('1', 1, TypeError),
        (1, '1', TypeError),
        (Path('/tmp'), '1', TypeError),
    ]
)
def test_division_wrong_type(a, b, expected_exception):
    with pytest.raises(expected_exception):
        division(a, b)
