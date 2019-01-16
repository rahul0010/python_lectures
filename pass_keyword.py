"""
if [condition]:
    pass
"""
num1 = 20
if(num1 >= 20):
    pass
print(num1)

for i in range(1,11):
    print(i)
    if i == 5:
        break

for i in range(1,11):
    if(i == 5):
        continue
    print(i)