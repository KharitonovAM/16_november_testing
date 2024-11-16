import pytest
from src.calculate_daiscont import calculate_discont

def test_calculate_discont(good_price):
    assert calculate_discont(good_price[0], good_price[1], 10) == [11*0.9,22*0.9,33*0.9]




