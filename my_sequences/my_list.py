myList = ["one", 2, 'three']              # list with 3 items, has length 3
myList1 = []                              # list with 0 items, has length 0
print(myList)
print(myList1)
print("============================")

# They look similar, but they are different types
s = "100"
myNewList = [100]
i = 100
print(s)
print(myNewList)
print(i)
print(type(s))   # Output: <class 'str'>
print(type(myNewList))   # Output: <class 'list'>
print(type(i))    # Output: <class 'int'>
print("===========================")

# Accessing elements
print("Accessing elements")
my_list = [10, 20, 30, 40, 50]

first_element = my_list[0]  # Accessing the first element (index 0)
last_element = my_list[-1]  # Accessing the last element using negative indexing

print(first_element) # Output: 10
print(last_element)  # Output: 50
print("==============================")

# Getting the length of a list
print("Getting the length of a list")
my_list = [10, 20, 30, 40, 50]
length = len(my_list)

print(length)  # Output 5
print("=====================")

# Modifying elements
print("Modifying elements")
my_list = [10, 20, 30, 40, 50]
my_list[2] = 35 # Modifying the element at index 2 (third element)

print(my_list)   # Output: [10, 20, 35, 40, 50]
print("=============================")

# Adding an element using append() method (can add just one element at the end of the list)
print('Adding an element using "append()" method')
a_list = [1, 2, 3]
a_list.append(4)     # Adding the element 4 to the end of the list

print(a_list)  #Output [1, 2, 3, 4]
print("=============================")

# Adding elements using extend() method
print("Adding elements using 'extend()' method")
a_list = [1, 2, 3]
a_list.extend([4, 5])     # Adding multiple elements at the end of the list

print(a_list)  # Output: [1, 2, 3, 4, 5]
print("================================")

# Adding elements using += operator
print("Adding elements using '+=' operator")
a_list = [1, 2, 3]
new_elements = [10, "car", 30]
a_list += new_elements          # Adding different data type elements at the end of a_list

print(a_list)   # Output: [1,2, 3, 10, "car", 30]
print("===========================================")

# Inserting an element at a specific position using insert() method
print("Using 'insert()' method")
a_list = [1, 2, 3]
a_list.insert(1, 10)      # Inserting the element 10 at position 1

print(a_list) # Output [1, 10, 2, 3]
print("================================")

# Removing an element by value using remove() method
print("Removing an element by value")
my_new_list = [1, 2, 3, 4, 5]
my_new_list.remove(3)  # Remove the first occurrence of the value 3

print(my_new_list)  # Output [1, 2, 4, 5]
print("========================")

# Removing an element by index using 'del' keyword
print("Removing an element using 'del' keyword")
my_new_list = [1, 2, 3, 4, 5]
del my_new_list[1]      # Removes the element at index 1 (second element)

print(my_new_list)  # Output [1, 3, 4, 5]