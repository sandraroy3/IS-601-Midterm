from typing import List
from .calculation import Calculation

class Calculations:
    history: List[Calculation] = []  # use type hinting and calculations have list of calculation

    @classmethod # class method vs static vs istance method - class method 1 for 1 class 
    # ie here we need only 1 history
    # for instances, we pass in self, for class methods pass in cls, and to refer to history do cls.history and available only in this class
    # below are convenience methods and we don't repeat them anywhere else.
    def add_calculation(cls, calculation: Calculation):
        '''Add a new calculation to the history'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Retreive the entire history of calculations'''
        return cls.history
    
    @classmethod
    def clear_history(cls):
        ''' clear the history of calculations'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''Get latest calculation, returns None if there's no history'''
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str):
        '''Find and return list of calculations by operation name'''
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]