#test_mathlib.py
import mathlib
import pytest


def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == 9

def test_calc_multiply():
    result = mathlib.calc_multiply(3, 10)
    assert result == 30

def test_my_function():
    res = mathlib.my_function(2, 3)
    assert res == 3.605551275463989
    
    with pytest.raises(ValueError):
        mathlib.my_function(10, 1)


def test_are_we_in_future():
    assert mathlib.are_we_in_future() == False     


def test_class():
    val = mathlib.AdderWithSaturation()
    val.add(2)
    assert val.value == 2
    
    val.add(11)
    assert val.value == 10        

       

