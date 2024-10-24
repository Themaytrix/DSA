def rotate(arr,k):
    
    # initialize temp array
    temp = [0] * len(arr)
    
    for i in range(len(arr)):
        if i+k >= len(arr):
            temp[(i+k)%len(arr)] = arr[i]
        else:
            temp[i+k] = arr[i]
    
    return temp

arr = [1,2,3,4,5]


# print(rotate(arr,2))