'''Testing Operations'''
from decimal import Decimal

import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('10'), Decimal('20'), add)
    assert calculation.perform() == Decimal('30'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('20'), Decimal('10'), subtract)
    assert calculation.perform() == Decimal('10'), "subtract operation failed"

def test_operation_multiply():
    '''Testing the multipy operation'''
    calculation = Calculation(Decimal('10'), Decimal('20'), multiply)
    assert calculation.perform() == Decimal('200'), "multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('20'), Decimal('10'), divide)
    assert calculation.perform() == Decimal('2'), "divide operation failed"

def test_operation_divide_by_zero():
    '''Testing the divide by 0 operation'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('20'), Decimal('0'), divide)
        calculation.perform()
