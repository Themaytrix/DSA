def recursive_sum(arr):
    sum = 0
    if arr == []:
        return sum
    else:
        return arr[0] + recursive_sum(arr[1:])
        
print(recursive_sum([2,4,6]))

# find maximum number in a list

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max