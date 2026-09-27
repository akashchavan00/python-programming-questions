# numbers = {1,2,3,4,5,5}
# print(numbers)

# +++++++++++++++++++++++++++++++++++++++++++

# s1 = {1,2,3}
# s2 = set([4,5,6,6,1])
# s3 = set("apple")
# print(s1)
# print(s2)
# print(s3)

# +++++++++++++++++++++++++++++++++++++++++++

# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange") # set operation to add an element to the set
# print(fruits)
# fruits.remove("banana") # set operation to remove an element from the set
# print(fruits)

# # If the item is not present, remove() raises an error.

# fruits.discard("banana")
# fruits.remove("banana")
# print(fruits)

# +++++++++++++++++++++++++++++++++++++++++++

# numbers = {1,2,3,3,4,5,6}

# print(len(numbers))

# ++++++++++++++++++++++++++++++++++++++++++++


"""
It is also possible to use the set() constructor to make a set.
"""

# thisset = set(("lily", "rose", "mogra", "sunflower")) # note the double round-brackets
# print(thisset)

# +++++++++++++++++++++++++++++++++++++++++++

# thisset = {"appple", "banana", "Cherry"}

# for item in thisset:
#     print(item)

# print("Cherry" in thisset)
# print("mango" in thisset)

# +++++++++++++++++++++++++++++++++++++++++++

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# set1.update(set2) # set operation to update the set with another set
# print(set1)

# +++++++++++++++++++++++++++++++++++++++++++

# Frozenset:
# A frozenset is a set that is immutable, meaning that you cannot change its elements after it has been created. This makes frozensets useful for situations where you need a set that should not be modified, such as when using sets as keys in dictionaries.

x = frozenset({1,2,3})
print(x)
print(type(x))