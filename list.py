newList = [5,3,1,7,4,2] #numeric list
print(newList)
newList.append(6) #append method to add element at last position
print(newList)
newList.pop()   # deletes the last element
print(newList)
newList.remove(3)
print(newList)
newList.sort()
print(newList)
newList.reverse()
print(newList)
print(newList.index(7))

mixed_list = [1,'hello',56,"world",[5,24,3,7]]
print(mixed_list)

for item in mixed_list:
    print(item)

print(10 not in mixed_list)