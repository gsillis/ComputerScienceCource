
from maximum import calculate_maximum

def test_when_calculate_maximum_is_called_should_return_maximum_number ():
    sut = calculate_maximum(10, 15)
    assert  sut == 15

def test_when_calculate_maximum_is_called_passing_two_zeros_should_return_zero ():
    sut = calculate_maximum(0, 0)
    assert  sut == 0

def test_when_calculate_maximum_is_called_passing_negative_number_should_return_positive_one ():
    sut = calculate_maximum(-1, 0)
    assert  sut == 0