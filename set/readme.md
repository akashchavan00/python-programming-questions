Unordered collections of unique values

- stores items with unique values
- it is mutable means you can add or remove items
- it is not indexed like a list
- it is commonly used for membership tests, removing duplicates and mathematical set operations

+++++++++++++++
Unordered:

Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be refereed to by index or key.

++++++++++++++++

Unchangeable:

We cannot change the items after the set has been created.

+++++++++++++++++

Duplicates not allowed.

The values True and 1 are considered the same value in sets and are treated as duplicates.

+++++++++++++++++

len(): To determine how many items a set has

+++++++++++++++++

Data types:

Set items can be of any data type: String, int, boolean
Set can contain different data types

From python's perspective sets are defined as objects with the data type 'set'.

++++++++++++++++++

Python collections (Arrays)

There are four collection data types in the python programming language:

List: Collection which is ordered and changeable. Allowws duplicate members.
Tuple: ordered ad unchangeable. Allows duplicate.
Set: unordered and unchangeable and unindexed. no duplicates
Dictionary: ordered and changeable no duplicate members.

+++++++++++++++++++

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"appple", "banana", "Cherry"}

for item in thisset:
    print(item)

print("Cherry" in thisset)
print("mango" in thisset)

++++++++++++++++++++++++

Add Sets:
To add items from another set into the current set, use the update() method.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

set1.update(set2) # set operation to update the set with another set
print(set1)

Add any iterable:
the object in the update() method does not have to be a set it can be any oterable object(tuples, lists, dictionaries etc.)

+++++++++++++++++++++++++

remove items:

You can also use the pop() method to remove an item, but this method will remove a random item so you cannot be sure what item that gets removed.

The clear() method empties the set.

The del keyword will delete the set completely:

del setname

++++++++++++++++++++++++++++

Join sets

There are several ways to join two or more sets in Python.

1. The union() and update() methods joins all items from both sets.
2. The intersection() method keeps ONLY the duplicates.
3. The difference() method keeps the items from the first set that are not in the other set(s).
4. The symmetric_difference() method keeps all items EXCEPT the duplicates.


-The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method. same for & - and ^
-The union() method returns a new set with all items from both sets.
-The update() changes the original set, and does not return a new set.
-The intersection() method will return a new set, that only contains the items that are present in both sets.
-You can use the & operator instead of the intersection() method, and you will get the same result.
-You can use the - operator instead of the difference() method, and you will get the same result.
-The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
-You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

+++++++++++++++++++++++++++++

Python frozenset

Immutable version of set
Like sets it contains the unique, unordered,uchangeable elements
unlike sets, elements cannot be added or removed from a frozenset.

Creating a frozenset 
use the frozenset() constructor to create a fronzenset from any iterable.

Frozenset Methods
Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

Method	                    Shortcut	Description	
copy()	 	                            Returns a shallow copy	
difference()	                -	    Returns a new frozenset with the difference	
intersection()	                &	    Returns a new frozenset with the intersection	
isdisjoint()	 	                    Returns True if there is NO intersection between two frozensets	
issubset()	                 <= / <	    Returns True if this frozenset is a (proper) subset of another	
issuperset()	             >= / >	    Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	        ^	    Returns a new frozenset with the symmetric differences	
union()	                        |	    Returns a new frozenset containing the union
