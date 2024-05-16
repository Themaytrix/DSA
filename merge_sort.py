def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2 #find the midpoint for d&c
    # split arrays into left and right
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    
    merge(left_arr,right_arr,arr)
    
    return arr
    

def merge(a,b,arr):
    # intialize pointers
    i=0
    j=0
    k=0
    
    while i<len(a) and j<len(b):
        # compare i and j index elements to see which is smaller
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        
        else:
            arr[k] = b[j]
            j += 1
            
        k += 1
    while i<len(a):
        arr[k] = a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k] = b[j]
        j+=1
        k+=1
    

data = [3,6,2,1,9,8,0,0]
test_case = [
    data,
    [],
    [1],
    [2,3],
    [5,6,10,1,9]
]
for r in test_case:
    print(merge_sort(r))
# print(len(new))     