'''My calculation test'''

from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that addition works'''
    assert add(2,4) == 6

def test_subtraction():
    '''Test that subtraction works'''
    assert subtract(6, 4) == 2

def test_multiplication():
    '''Test that multiplication works'''
    assert multiply(2,4) == 8

def test_division():
    '''Test that division works'''
    assert divide(2,4) == 0.5
