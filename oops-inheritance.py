"""
derived class inherits the property and behaviour of parent class
parent class: main class or the class having super method
derived class: this class inherits property of parent class

syntax: 
    class Parent:
        [properties and methods]
    
    class Child(Parent):
        [properties and methods]

objname = Child([arguments])
"""
class Animal:  
    def speak(self):  
        print("Animal Speaking")  

class Dog(Animal):  
    def bark(self):  
        print("dog barking") 

class DogChild(Dog) :
    def eat(self):
        print("Dog is eating")

dog = DogChild()
dog.bark()
dog.speak()
dog.eat()