# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Brute Force


def elseProduct(lst):
    arr = []
    for i in range(len(lst)):
        val = 1
        for j in range(len(lst)):
            if(i != j):
                val *= lst[j]
        arr.append(val)
    return arr

# Using division


def elseProduct2(lst):
    total = 1
    arr = []
    for x in lst:
        total = total*x
    for i in range(len(lst)):
        arr.append(total/lst[i])
    return arr


print(elseProduct2([1, 2, 3, 4, 5]))
