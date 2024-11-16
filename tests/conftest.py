import pytest

@pytest.fixture
def tax_value():
    return 0

@pytest.fixture
def bad_price():
    return [0,-5,'asfsdf']

@pytest.fixture
def bad_price_again():
    return [10,20,'asfsdf']

@pytest.fixture
def wrong_tax():
    return -20