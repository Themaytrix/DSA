def recursive_sum(arr):
    sum = 0
    if arr == []:
        return sum
    else:
        return arr[0] + recursive_sum(arr[1:])
        
print(recursive_sum([2,4,6]))