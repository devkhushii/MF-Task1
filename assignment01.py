#creating a list
list=[12,34,5,34,67,89]

#operations on list

# Add elements to the list
list.append(9)
print("List after adding elements:", list)
# Modify an element
list[1] = 4
print("List after modifying an element:", list)
# Remove an element
list.remove(4)
print("List after removing an element:", list)
# Insert an element at a specific position
list.insert(1, 5)
print("List after inserting an element:", list)
# Remove an element by index
del list[0]
print("List after removing an element by index:", list)
# Find the index of an element
index = list.index(5)
print("Index of element 4:", index)
# Check if an element is in the list
print("Is 5 in the list?", 5 in list)
# Length of the list
print("Length of the list:", len(list))
# Clear the list
list.clear()
print("List after clearing:", list)

# Creating an empty dictionary
my_dict = {}
# Adding elements to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['gender'] = 'Male'
print("Dictionary after adding elements:", my_dict)
# Modifying an element
my_dict['age'] = 32
print("Dictionary after modifying 'age' element:", my_dict)
# Removing an element
removed_element = my_dict.pop('gender')
print("Dictionary after removing 'gender' element:", my_dict)
print("Removed element:", removed_element)

# Create an empty set
my_set = set()
# Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("Initial set:", my_set)
# Remove an element from the set
my_set.remove(2)
print("Set after removing 2:", my_set)
# Modify an element in the set
if 3 in my_set:
    my_set.remove(3)
    my_set.add(4)
print("Set after modifying 3 to 4:", my_set)
