"""
functions are block of statements that can be executed when called at certain line of program. 
Functions may or may not return value
syntax

def function_name([parameters]):
    [block of statement]
    return 0
"""
def add(a,b):
    return a+b

def displayMessage(name:str):
    print("Welcome! " + name)

def showMessage():
    print("Hello world")

def returnVal():
    return "Hello"

num1 = 5
num2 = 10
total = add(num1, num2)
displayMessage("Rahul")
print(total)
showMessage()
returnedVal = returnVal()