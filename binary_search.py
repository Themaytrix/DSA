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

data = [1,2,3,4,5,6,7,8,9]  
# print(len(data))
      
# print(rec_binary_search(data,4,0,len(data)-1))

def find_combinations(arr, k, n):
    def backtrack(start, path, target):
        # Base case: when the path length is k and target is 0, we have a valid combination
        if len(path) == k:
            if target == 0:
                results.append(path[:])
            return
        
        # Iterate through the array to build combinations
        for i in range(start, len(arr)):
            # If the current element exceeds the target, stop (since the array is sorted)
            if arr[i] > target:
                break
            
            # Include the current element and recurse
            path.append(arr[i])
            backtrack(i + 1, path, target - arr[i])
            path.pop()  # Backtrack by removing the last element

    arr.sort()  # Ensure the array is sorted for binary-search-like logic
    results = []
    backtrack(0, [], n)
    return results

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 2
n = 8
print(find_combinations(arr, k, n))


        
    
        

        
        
print(3//2)