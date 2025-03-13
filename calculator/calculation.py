class Calculation:
    def __init__(self, a, b, operation): # self is pointer to same class
        self.a = a 
        self.b = b
        self.operation = operation
        
    def get_result(self):
        return self.operation(self.a, self.b)