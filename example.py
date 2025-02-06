def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # do not change this line until prompted to do

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    assert add(2.5, 2.5) == 5.0 
