"""
OOP = Object Oriented Programming

Features:
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

Class : Blueprint or skeleton
object: Instance of class

1. attributes
2. Behaviour 

syntax: 
    class classname:
        [properties and methods]

objname = classname([arguments])
"""
class parrot:
    def __init__(self):
        self.color = "blue"
        self.song = "drive"
    
    def action(self):
        return "The "+ self.color +" parrot sings " +self.song

p = parrot()
print(p.color)
print(p.action())