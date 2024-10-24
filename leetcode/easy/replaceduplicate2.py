def repduplicates(arr):
    
    if len(arr) <= 2:
        return arr
    
    j = 1
    
    for i in range(2,len(arr)):
        if arr[i] != arr[j-1]:
            j+=1
            arr[j] = arr[i]
    return j+1