"""
Multiple inhertance: A derived (child) class inherits properties from multiple base (parent) class

syntax: 
    class Parent1:
        [properties and methods]
    
    class Parent2:
        [properties and methods]
    
    class Child(Parent1, Parent2):
        [properties and methods]

objname = Child([arguments])
"""

class Calculation1:  
    def Summation(self,a,b):  
        return a+b  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b  

d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  