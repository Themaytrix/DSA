    
def binary_search(list,target):    
    """Binary Search:
        - Input list has to be sorted
        - First search is done by hitting the midpoint of the list.
        -Eliminate portion that is greater than or less than target.
        -repeat process till you achieve number
    """
    
    low = 0
    high = len(list) + 1
    
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
        
        