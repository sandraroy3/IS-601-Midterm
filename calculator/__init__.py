# Class for modules and namespace 

from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
    # Callable means, and purposefully makes fn break if not used correctly w/o using if statement
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()    

    @staticmethod #static method means access to only params passed to them
    def add(a: Decimal, b: Decimal) -> Decimal:  # fn signature, decimal is type hinting
        return Calculator._perform_operation(a, b, add) # _ in method means not public and only in calss

    @staticmethod 
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod 
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)
        
    @staticmethod 
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)