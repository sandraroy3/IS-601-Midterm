# Class for modules and namespace 

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod # functions, and fn in class is method, 
    # static method - globally accessible - but not used in classes/instances
    # perform actions, 
    def add(a,b):
        calculation = Calculation(a, b, add) # instance and pass the add fn from the
        return calculation.get_result()

    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a, b, multiply)
    
        return calculation.get_result()
    
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)
        return calculation.get_result()