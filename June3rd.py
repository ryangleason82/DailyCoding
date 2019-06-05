# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


# My first approach is simple.
# Sort the array, find if num at index i + 1 - index at i is greater than 1
# If it is, return, if not add one to the last element of the array

def lowestInt(arr):
    new = sorted(arr)
    for i in new:
        if new[i] > 0:
            if (new[i+1]-new[i] > 1):
                return (new[i] + 1)
    return (new.pop() + 1)


# My second approach uses the linked list runner method
# Keep the runner one node in front of the current
# If runner - current > 1, return current + 1
# Otherwise, return last node + 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def llLowestInt(self, arr):
        curr = self.head
        runner = curr.next

        while(runner):
            if(curr > 0):
                if(runner - curr > 1):
                    return curr + 1
        return runner + 1


print(lowestInt([3, 4, -1, 1]))


# The key to this problem was mapping it to the indices. Two solutions are below.w
# Sorting was a bad idea because it takes O(nlogn) and we can't have that.

def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

# This is very simple and I'm a little mad I didn't think of it. Iterates through and
# if the index exists in the array it goes until it doesn't.. returns missing one


def first_missing_positives(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i
