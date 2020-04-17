from math_series.series import fibonacci
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



