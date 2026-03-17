import pytest
from lab import get_even_numbers, find_max


def test_get_even_numbers():
    assert get_even_numbers([1,2,3,4,5,6]) == [2,4,6]
    assert get_even_numbers([1,3,5]) == []


def test_find_max():
    assert find_max([1,5,3]) == 5


def test_find_max_empty():
    with pytest.raises(ValueError):
        find_max([])