"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(arr,target):
    # instantiate a hashtable
    numhash = {}
    
    for i,n in enumerate(arr):
        othersum = target - n
        
        if othersum in numhash:
            return [numhash[othersum],i]
        numhash[n] = i
        
num = [2,3,2]

indices =two_sum(num,4)

print(indices)
