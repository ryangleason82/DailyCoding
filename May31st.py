# Given a list of numbers and number k, return whether any two numbers from the list add up to k
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Brute Force Approach


def isThereASum(arr, k):
    for i in arr:
        (print(i))
        for j in arr:
            print(j)
            if (i + j == k):
                print(i, j)
                return True


# Dictionary Approach
def isThereASum2(arr, k):
    sumDict = {}
    for i in range(len(arr)):
        for j in range(len(arr)):
            sumDict[arr[i]] = (arr[i]+arr[j])
    print(sumDict.items())
    return (k in sumDict.values())


print(isThereASum2([10, 15, 3, 7], 17))

# Correct Solution
