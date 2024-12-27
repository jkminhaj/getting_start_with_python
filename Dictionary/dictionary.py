# Basics of Dictionaries in Python

# 1. Creating a Dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
empty_dict = {}  # Empty dictionary
dict_from_list = dict([("name", "Bob"), ("age", 30)])  # From a list of tuples
print("Original Dictionary:", my_dict)
print("Empty Dictionary:", empty_dict)
print("Dictionary from List of Tuples:", dict_from_list)

# 2. Accessing Values
print("\nAccessing Values:")
print("Name:", my_dict["name"])  # Using key
print("Age:", my_dict.get("age"))  # Using get()

# 3. Adding and Updating Values
my_dict["profession"] = "Engineer"  # Adding a new key-value pair
my_dict["age"] = 26  # Updating an existing value
print("\nAfter Adding/Updating Values:", my_dict)

# 4. Removing Items
removed_value = my_dict.pop("city")  # Removes and returns the value
print("\nAfter Removing 'city':", my_dict)
print("Removed Value:", removed_value)

# Using del to remove a key
del my_dict["age"]
print("After Removing 'age' with del:", my_dict)

# Clearing all items
my_dict.clear()
print("After Clearing Dictionary:", my_dict)

# 5. Dictionary Operations
example_dict = {"a": 1, "b": 2, "c": 3}

# Keys, Values, and Items
print("\nKeys:", example_dict.keys())
print("Values:", example_dict.values())
print("Items:", example_dict.items())

# Checking Key Existence
print("\nIs 'a' a key in the dictionary?", "a" in example_dict)
print("Is 'z' a key in the dictionary?", "z" in example_dict)

# Iterating Through a Dictionary
print("\nIterating Through Dictionary:")
for key, value in example_dict.items():
    print(f"{key}: {value}")

# 6. Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
}
print("\nNested Dictionary:")
print(nested_dict)
print("Accessing Nested Value (person1's age):", nested_dict["person1"]["age"])

# 7. Dictionary Comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print("\nDictionary Comprehension (Squares):", squared_dict)
