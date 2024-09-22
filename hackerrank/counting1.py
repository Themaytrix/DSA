def countingSort(arr):
    temp_arr = [0] * len(arr)
    
    # loop throgh arr to
    
    for i in arr:
        temp_arr[i] += 1
    
    return temp_arr

arr = [1,1,3,2,1,2]

print(countingSort(arr))        