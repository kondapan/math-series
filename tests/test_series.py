from math_series.series import fibonacci
from math_series.series import lucas

def test_0():
    fb = fibonacci(0)
    assert 0 == fb

def test_1():
    fb = fibonacci(1)
    assert 1 == fb

def test_2():
    fb = fibonacci(2)
    assert 1 == fb

def test_3():
    fb = fibonacci(3)
    assert 2 == fb

def test_4():
    fb = fibonacci(4)
    assert 3 == fb

def test_5():
    fb = fibonacci(5)
    assert 5 == fb

def test_6():
    fb = fibonacci(6)
    assert 8 == fb


def test_l_0():
    fb = lucas(0)
    assert 2 == fb

def test_l_1():
    fb = lucas(1)
    assert 1 == fb

def test_l_2():
    fb = lucas(2)
    assert 3 == fb

def test_l_3():
    fb = lucas(3)
    assert 4 == fb

def test_l_4():
    fb = lucas(4)
    assert 7 == fb

def test_l_5():
    fb = lucas(5)
    assert 11 == fb

def test_l_6():
    fb = lucas(6)
    assert 18 == fb

