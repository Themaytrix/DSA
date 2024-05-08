#Implementation of a queue with Arrays

front_of_queue = -1
rear_of_queue = -1

#check if queue is empty
def is_empty(arr):
    #check if front and rear are still at -1
    if front_of_queue == -1 and rear_of_queue == -1:
        return True
    else:
        return False
    
#check if queue is full
def is_full(arr):
    #check if the rear index points the last index of the array
    if (rear_of_queue + 1)%len(arr)-1 == front_of_queue:
        print('Queue if full')
        return True

def enqueue(arr,x):
    if is_full(arr):
        return
    elif is_empty(arr):
        front_of_queue = rear_of_queue = 0 
        arr[rear_of_queue] = x
    else:
        rear_of_queue = (rear_of_queue + 1)%len(arr)
        arr[rear_of_queue] =x
        
def dequeue(arr):
    if is_empty(arr):
        return
    elif front_of_queue == rear_of_queue:
        rear_of_queue = front_of_queue =-1
    else:
        front_of_queue = (front_of_queue +1) % len(arr)
        
        
        