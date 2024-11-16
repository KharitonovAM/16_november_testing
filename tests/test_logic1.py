import pytest
from src.logic1 import calculate_taxes
def test_calculate_taxes():
    assert calculate_taxes([20.0],20.0) == [24.0]


@pytest.mark.parametrize('list_prices,tax,expect',[([10,20,30],10,[11,22,33]),
                                                   ([40,50,60],20,[48,60,72])])
def test_calculate_texes_using_parametrize(list_prices,tax,expect):
    assert calculate_taxes(list_prices,tax) == expect


def test_bad_tax_value(tax_value):
    assert calculate_taxes([10,20,30],tax_value) == [10,20,30]


def test_bad_price(tax_value, bad_price):
    with pytest.raises(ValueError):
        calculate_taxes(bad_price,tax_value)


def test_bad_price(tax_value, bad_price_again):
    with pytest.raises(TypeError):
        calculate_taxes(bad_price_again,tax_value)


def test_bad_tax_value(wrong_tax):
    with pytest.raises(ValueError) as e:
       calculate_taxes([10,20,30],wrong_tax)
    print(e.value)
    assert str(e.value) == str(ValueError('Неверный налоговый процент'))