"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

def searchindexposition(arr, target):
    # split the arr into a midpoint
    
    low = 0
    high = len(arr)-1
    if target > arr[high]:
        return len(arr)
    
    while low <= high:
        midpoint = (low + high) // 2
        if target == arr[midpoint]:
            return midpoint
        elif target > arr[midpoint]:
            low = midpoint + 1
        else:
            high =midpoint -1
    return low

arr = [1,3,5,6]

print(searchindexposition(arr,2))
        