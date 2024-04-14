#ITERATIVE    
    
def binary_search(list,target):    
    """Binary Search:
        - Input list has to be sorted
        - First search is done by hitting the midpoint of the list.
        -Eliminate portion that is greater than or less than target.
        -repeat process till you achieve number
    """
    
    low = 0
    high = len(list) - 1
    
    while low <= high:
        midpoint = (low + high)//2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            # if the midpoint or guess is greater than target number we eliminate all items above it and set a new high to be the midpoint
            high = midpoint -1 
        else:
            low = midpoint + 1
            

    return None


#RECURSIVE

def rec_binary_search(wordlist,key,low,high):
   #Base Case- check if low is lower than high. i.e list contains a single element
    if low <= high:
            
        midpoint = (low + high) // 2
        if key == wordlist[midpoint]:
            return midpoint
        elif key < wordlist[midpoint]:
            return rec_binary_search(wordlist,key,low,midpoint-1)
        else:
            return rec_binary_search(wordlist,key,midpoint+1,high)
    else:
        return None

data = [1,2,3,4,5,9,10,12]        
print(rec_binary_search(data,4,0,len(data)-1))

        
        