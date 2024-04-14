def quicksort(array,low,high):
    if low<high and len(array) > 1:
        partition_index = partition(array,low,high)
        quicksort(array,low,partition_index-1)
        quicksort(array,partition_index+1,high)
        return array
    else:
        return array
    
def partition(array,low,high):
    pivot = array[low]
    i=low
    j=high
    
    while i<j:
        while array[i] <= pivot and i<j:
            i +=1
        while array[j] > pivot and i<j:
            j -=1
        if(i<j):
            array[i],array[j] = array[j],array[i]
    if array[j] < pivot:
        array[low],array[j] = array[j],array[low]
    return j
            
        
data = [10,6]
test_case = [
    [0],
    [],
    [8,2],
    [5,10,66,24,14,2,3,1,88]
]
for r in test_case:
    
    print(quicksort(r,0,len(r)-1))

# print(quicksort(data,0,len(data)-1))