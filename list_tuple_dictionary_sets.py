# list in python  and list is mutable means we can change the vaule using ind
# student=["shivam",99,17,"delhi"]
# print(student[0])
# student[0]="pandey"
# print(student[0])
# print(student)

# list slicing {similar to that of the string slicing}  {the last index is not included in the slicing...}
# marks=[87,64,33,95,76]
# print(marks[1:4])
# print(marks[:4])
# print(marks[0:])
# print(marks[0:len(marks)])
# print(len(marks))

# list methods...
list = [2,1,3]
list.append(4) #adds one element at end
print(list)

list.sort() # in the complete list is got sorted it also work for the alphabte in ascending order.
print(list)

list.sort(reverse=True) # here in these we got the sorted in reverse order...
print(list)

list.reverse() #reverse the given list..
print(list)

list.insert(0,0) # here these insert method used for the insertion of the element at the specific index ... first is index and the second one is value..
print(list)


list.remove(2) # here these remove method is used for the removal of the value from the list it removes the value occuring first 
print(list)

list.pop(2) # here in these it remove the value at the specific index we will write their... 
print(list)

list[0]=3  # here in list we can change the value using the indexing... 
print(list)

# tuples in python....
