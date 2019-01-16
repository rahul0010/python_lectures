"""
Conditonal Statements
1. If statement
2. If-else
3. if-elif-else

Syntax:
1. if statement
    if [condition]:
        [block of statements]

2. if-else
    if [condition]:
        [block of statements]
    else:
        [block of statements]
    
3. if-elif-else
    if [condition_1]:
        [block of statement]
    elif [condition_2]:
        [block of statement]
    .
    .
    .
    elif[condition_n]:
        [block of statement]
    else:
        [block of statement]
"""
num1 = int(input("Enter your percentage: "))

# if num1<=100:
#     print("%d is under %d"%(num1,100))
# else:
#     print("%d is not under %d"%(num1,100))

if num1>=75:
    print("Grade A")
elif num1>=50 and num1<75:
    print("Grade B")
elif num1>=35 and num1<50:
    print("Grade C")
else:
    print("Failed")




 







