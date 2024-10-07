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
my_list = [10, 20, 30, 40, 50]

first_element = my_list[0]  # Accessing the first element (index 0)
last_element = my_list[-1]  # Accessing the last element using negative indexing

print(first_element) # Output: 10
print(last_element)  # Output: 50
print("==============================")

# Modifying elements
my_list = [10, 20, 30, 40, 50]
my_list[2] = 35 # Modifying the element at index 2 (third element)

print(my_list)   # Output: [10, 20, 35, 40, 50]
print("=============================")

