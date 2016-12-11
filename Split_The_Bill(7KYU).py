# -*- coding: UTF-8 -*-
from collections import OrderedDict

group = {
    'A': 20,
    'B': 15,
    'C': 10
}

def split_the_bill(x):
    total_each_owed = sum(x.values())/float(len(x))
    return {key:round(value - total_each_owed, 2) for key, value in x.items()}

print split_the_bill(group)


'''
It's tricky keeping track of who is owed what when spending money in a group. Write a function to balance the books.

The function should take one parameter: an object/dict with two or more name-value pairs which represent the members of the group and the amount spent by each.
The function should return an object/dict with the same names, showing how much money the members should pay or receive.
Further points:

The values should be positive numbers if the person should receive money from the group, negative numbers if they owe money to the group.
If value is a decimal, round to two decimal places.
Translations and comments (and upvotes!) welcome.

Example

3 friends go out together: A spends £20, B spends £15, and C spends £10. The function should return an object/dict showing that A should receive £5, B should receive £0, and C should pay £5.

group = {
    'A': 20,
    'B': 15,
    'C': 10
}

split_the_bill(group) # returns {'A': 5, 'B': 0, 'C': -5}

'''