from decimal import Decimal
from typing import Callable


class Calculation:
    # instance methods - work on copies of class
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]): # self is pointer to same class, 
        # also called constructor
        self.a = a 
        self.b = b
        self.operation = operation
        
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''factory method - factory for instances or to create instances'''
        return Calculation(a, b, operation)
    
    def perform(self) -> Decimal:
        '''Perform stored calculation and return the result'''
        return self.operation(self.a, self.b)
    
    def __repr__(self):
        '''Return a simplified string representation of the calculation'''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
    