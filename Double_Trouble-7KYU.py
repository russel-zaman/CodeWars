def trouble(x, t):
    i = 0
    while i < len(x) - 1:
        if x[i] + x[i+1] == t:
            del x[i+1]
        else:
            i += 1
    return x




lst = [1, 3, 5, 6, 7, 4, 3]
tst = 7

print trouble(lst,tst)

"""
Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.

Example:

x = [1, 2, 3, 4, 5]
t = 3

1+2 = t, so remove 2. No other pairs = t, so rest of array remains:

[1, 3, 4, 5]

Work through the array from left to right.

Return the resulting array.

"""