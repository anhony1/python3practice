# List

myList = ["banana", "apple", "pears"]

# prints all items in the list 
print(myList)

# prints one item in the list
print(myList[1])

# adds element to the end of the list
myList.append("tomatoe")

print(myList)

# clears all items in the list
myList.clear()

print(myList)

#returns a copy of a list

newList = [1,1,1,1,2,3,4,5]

myList = newList.copy()

print(myList)

# returns the count of a specific element in a list

print("there are: ", myList.count(1), " 1's in this list")

newList2 = ["shoe", "cow"]

# extend adds a list to the end of another

myList.extend(newList2)

print("Extended list with shoe and cow: ", myList)

# index returns the value at a specified location

print("Index of 4: ", myList.index(4))

# inserts value at a specifc location

myList.insert(0, "FRONT")

print("insert 'FRONT' into front: ", myList)

# removes element at a specific location

myList.pop(0)

print("remove [0]: ", myList)

# reverse order of list

myList.reverse()

print("reverse: ", myList)

# sort order of list

myList.pop(0)

myList.pop(0)

myList.sort()

print("sort: ", myList)










