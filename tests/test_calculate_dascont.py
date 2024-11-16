import pytest
from src.calculate_daiscont import calculate_discont

def test_calculate_discont(good_price):
    assert calculate_discont(good_price[0], good_price[1], 10) == [11*0.9,22*0.9,33*0.9]

def test_len_of_rezult(good_price, len_of_rezult):
    assert calculate_discont(good_price[0], good_price[1], 0, len_of_rezult) == [11.000,22.000,33.000]

def test_right_types(good_price,len_of_rezult, wrong_type):
    with pytest.raises(TypeError):
        assert calculate_discont(wrong_type, good_price[1], 0, len_of_rezult)
        assert calculate_discont(good_price[0], wrong_type, 0, len_of_rezult)
        assert calculate_discont(good_price[0], good_price[1], wrong_type,len_of_rezult)
        assert  calculate_discont(good_price[0], good_price[1], disc=0, wrong_type)






