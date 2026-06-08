# Lists and Tuples Practice

# Lists
# A List is ordered, mutable collection of items.

# Integer List
# All items inside the list are integers.
list_Int = [1,5,8,54]
# String List
# All items inside the list are strings.
list_Str = ["Hello", "Hi", "Bye"]
# Mixed data type list
# Can contain multple data type items.
list_mixed =["Hello","Hi",6,98]

# Nested list
# Lists inside list
matrix = [[1,6],[87,73]]

# List Indexing
# Indexing in lists is same as indexing used in strings.
list_a = [24,8,82,4]
# 24 is at index 0, 8 is at index 1, and so on.
print(list_a[0]) # Output: 24
print(list_a[3]) # Output: 4

# Negative indexing
# Negative indexing starts from end of the list. Last element get index position of -1, last before gets index position of -2 , and so on.
print(list_a[-1]) # Output: 4
print(list_a[-4]) # Output: 24

# List Slicing
# We can extract any part of list by using list slicing.
# Syntax of list slicing is list_name[start index : end index].
# Start index is inclusive and end index is exclusive.
print(list_a[0:3]) # Output: [24,8,82]

# Lists are mutable.
# We can change items in lists.
list_b = [73,83,6,8,37,2]
list_b[3] = 4
print(list_b) # Output: [73,83,6,4,37,2]

# List Methods

# 1. append() - Adds element to end of the list.
list_a = [24,8,82,4]
list_a.append(46)
print(list_a)
list_b.append(56)
print(list_b)

# 2. extend() - Adds multiple elements.
list_a.extend([48,58])
print(list_a)

# 3. insert() - insert element in specified index position.
# syntax - insert(index,element) this inserts the element in specified position.
list_c = [1,4,7]
list_c.insert(1,9)
print(list_c)

# 4. remove() - removes first ocurence element.
list_d = [1,6,3,8,3]
list_d.remove(3)
print(list_d)

# 5. pop() - removes element by sepecified index position.
# By default it removes last element.
list_d.pop(2)
print(list_d)

# clear() - this function clears the entire list leading to empty list.
list_d_1 = [63,87,9,2]
list_d_1.clear()
print(list_d_1)

# index() - used to find index of elements.
list_e = [2,3,6,3,8]
print(list_e.index(3))

# count() - used to count how many time a element is occured in the list.
print(list_e.count(3))

# sort() - sorts the elements in a list in ascending order.
list_e.sort()
print(list_e)

# reverse() - used to reverse the elements in a list.
list_e.reverse()
print(list_e)

# List Comprehension
# Short and clean way to create lists.
# Syntax - [expression for item in iterable]
# Example: To sqaure elements in a list
# Using loop
nums = [2,4,5]
squares = []
for i in nums:
    squares.append(i**2)
print(squares)
# Using list comprehension
nums = [2,4,5]
squares = [x**2 for x in nums]
print(squares)

# Accessing items in Nested lists 
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2]) 
print(matrix[2][2])

# Tuples
# Tuple is a ordered immutable collection of items.
t = (2,7,4) # This is an examle of tuple.
t = (5) # This is not a tuple , it is an integer.
print(type(t))
t = (5,) # This is an tuple.
print(type(t))

# Accessing Tuple
# As usal we access tuple by its index positions.
t = (2,7,4)
print(t[1])

# Tuple slicing
# Syntax - tuple_name(start_index:end_index)
# start index is inclusive, end index is exclusive.
t_1 = (3,6,4,2,8,5)
print(t_1[2:5])

# Tuples are immutable(cannot be modified once they are created).
# t_1[4] = 1 gives an error.

# Tuple methods
# 1. count() - used to count how many times a element is occured in tuple .
t_2 = (1,2,2,2,3)
print(t_2.count(2))
# 2. index() - used to find position of items in tuple.
print(t_2.index(2))

# Tuple Packing
t = 10, 20, 30
print(t) # python automatically creates tuple

# Tuple unpacking.
t = 10, 20, 30
a,b,c = t
print(a)
print(b)
print(c)

# We cannot modify tuple but we can modify list present in tuple.
t = (10,20,30,[40,50])
t[3][1] = 60
print(t)
