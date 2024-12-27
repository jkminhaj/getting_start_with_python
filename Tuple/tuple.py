# Basics of Tuples in Python

# 1. Creating a Tuple
my_tuple = (1, 2, 3, 4)
empty_tuple = ()
single_element_tuple = (5,)  # Note the comma for single element
tuple_from_list = tuple([1, 2, 3])
print("Original Tuple:", my_tuple)
print("Empty Tuple:", empty_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Tuple from List:", tuple_from_list)

# 2. Accessing Elements
print("\nAccessing Elements:")
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# 3. Slicing
print("\nSlicing Tuples:")
print("First 3 Elements:", my_tuple[:3])
print("Elements from Index 2:", my_tuple[2:])

# 4. Immutable Nature
# Tuples are immutable, so this will raise an error if uncommented
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 5. Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated Tuple:", concatenated_tuple)

# Repetition
repeated_tuple = tuple1 * 2
print("Repeated Tuple:", repeated_tuple)

# Membership Test
print("\nIs 2 in tuple1?", 2 in tuple1)
print("Is 7 in tuple2?", 7 in tuple2)

# 6. Tuple Unpacking
a, b, c = tuple1  # Unpack elements into variables
print("\nTuple Unpacking:")
print("a =", a, ", b =", b, ", c =", c)

# 7. Length of Tuple
print("\nLength of tuple1:", len(tuple1))

# 8. Nested Tuples
nested_tuple = (1, (2, 3), (4, 5))
print("\nNested Tuple:", nested_tuple)
print("Access Nested Element:", nested_tuple[1][1])  # Access 3

# 9. Using Tuples as Keys in Dictionaries
# Tuples are hashable and can be used as dictionary keys
coordinates = {(0, 0): "Origin", (1, 2): "Point A"}
print("\nDictionary with Tuple Keys:", coordinates)
print("Value for (1, 2):", coordinates[(1, 2)])
