from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_0():
    output = fibonacci(0)
    assert 0 == output

def test_1():
    output = fibonacci(1)
    assert 1 == output

def test_2():
    output = fibonacci(2)
    assert 1 == output

def test_3():
    output = fibonacci(3)
    assert 2 == output

def test_4():
    output = fibonacci(4)
    assert 3 == output

def test_5():
    output = fibonacci(5)
    assert 5 == output

def test_6():
    output = fibonacci(6)
    assert 8 == output


def test_l_0():
    output = lucas(0)
    assert 2 == output

def test_l_1():
    output = lucas(1)
    assert 1 == output

def test_l_2():
    output = lucas(2)
    assert 3 == output

def test_l_3():
    output = lucas(3)
    assert 4 == output

def test_l_4():
    output = lucas(4)
    assert 7 == output

def test_l_5():
    output = lucas(5)
    assert 11 == output

def test_l_6():
    output = lucas(6)
    assert 18 == output

def test_both_1():
    output = sum_series(0)
    assert 0 == output

def test_both_2():
    output = sum_series(0,2,1)
    assert 2 == output

def test_both_3():
    output = sum_series(0,0,1)
    assert 0 == output
