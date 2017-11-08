#test_mathlib.py
import mathlib2
import pytest


@pytest.mark.parametrize("test_input, expected_output",
                          [(5, 25), (9, 81), (10, 100)]
                        )
def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output


@pytest.mark.skipif(sys.version_info > (3,5), reason="I don't want to run this this test now")
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == 9


@pytest.mark.xfail()
def test_calc_multiply():
    result = mathlib.calc_multiply(3, 10)
    assert result == 30


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True  


@pytest.mark.mac
def test_mac_1():
    assert True 


@pytest.mark.mac
def test_mac_2():
    assert True           

    

       

