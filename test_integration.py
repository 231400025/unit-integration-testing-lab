import pytest
from bank_app import transfer, calculate_interest

def test_transfer():
    a, b = transfer(1000, 500, 200)
    assert a == 800
    assert b == 700

def test_transfer_and_interest():
    a, b = transfer(2000, 1000, 500)
    result = calculate_interest(b, 10, 1)
    assert round(result, 2) == 1650


def test_transfer_fail():
    with pytest.raises(ValueError):
        transfer(100, 500, 300)
