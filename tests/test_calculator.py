'''My Calculator Test '''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works- test functions and test file must start with 
    test_ for pytest lib to understand it is tests'''
    assert add(3,4) == 7
    # follow AAA(arrange, act, assert) testing: we arrange
    # ie import add in the above import line,
    # action is basically calling add(3,4) and then assert with its actual value 7


def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract(5,2) == 3
