import math

class AreaCalc:
    def calculate(self, arg1, arg2 = None):
        if arg2 == None:
            return round(math.pi * arg1**2, 2)
        else: 
            return arg1 * arg2
    


    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
