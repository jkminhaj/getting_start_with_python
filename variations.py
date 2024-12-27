# Demonstrating Differences Between List, Tuple, and Set

# 1. Creation
my_list = [1, 2, 3, 3]          # List allows duplicates
my_tuple = (1, 2, 3, 3)         # Tuple allows duplicates
my_set = {1, 2, 3, 3}           # Set removes duplicates

print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)

# 2. Mutability
my_list[0] = 10  # Lists are mutable
print("\nModified List:", my_list)

# Tuples are immutable; uncommenting the next line will cause an error
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

my_set.add(4)  # Sets are mutable (can add/remove elements)
print("Modified Set:", my_set)

# 3. Order and Indexing
print("\nAccessing Elements:")
print("List Element at Index 1:", my_list[1])  # Lists support indexing
print("Tuple Element at Index 1:", my_tuple[1])  # Tuples support indexing

# Sets do not support indexing
# Uncommenting the next line will cause an error
# print("Set Element at Index 1:", my_set[1])  # TypeError: 'set' object is not subscriptable

# 4. Unique Elements
unique_list = list(set(my_list))  # Convert list to set to remove duplicates
print("\nUnique Elements from List:", unique_list)

# 5. Operations
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Concatenation
print("\nConcatenation:")
print("List Concatenation:", list1 + [4, 5])  # Lists can be concatenated
print("Tuple Concatenation:", tuple1 + (7, 8))  # Tuples can be concatenated

# Sets do not support concatenation but support union
print("Set Union:", set1.union(set2))

# Membership Test
print("\nMembership Test:")
print("Is 2 in List?", 2 in list1)
print("Is 5 in Tuple?", 5 in tuple1)
print("Is 3 in Set?", 3 in set1)

# 6. Performance
import time

# List Lookup
start = time.time()
print(1000 in list(range(1000000)))  # Slower for lookups
end = time.time()
print("List Lookup Time:", end - start)

# Set Lookup
start = time.time()
print(1000 in set(range(1000000)))  # Faster for lookups
end = time.time()
print("Set Lookup Time:", end - start)
