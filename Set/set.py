# Basics of Sets in Python

# 1. Creating a Set
my_set = {1, 2, 3, 4}
empty_set = set()  # Empty set
set_from_list = set([1, 2, 3, 3])  # Removes duplicates
print("Original Set:", my_set)
print("Set from List:", set_from_list)

# 2. Adding Elements
my_set.add(5)
print("\nAfter Adding 5:", my_set)

# 3. Removing Elements
my_set.remove(3)  # Removes 3, raises KeyError if not found
print("After Removing 3:", my_set)

my_set.discard(6)  # Discards 6, no error if not found
print("After Discarding 6:", my_set)

# 4. Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print("\nUnion of set1 and set2:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference of set1 - set2:", difference_set)

# Symmetric Difference
symmetric_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_diff_set)

# 5. Subset and Superset
small_set = {1, 2}
print("\nIs small_set a subset of set1?", small_set.issubset(set1))
print("Is set1 a superset of small_set?", set1.issuperset(small_set))

# 6. Clearing a Set
my_set.clear()
print("\nAfter Clearing my_set:", my_set)
