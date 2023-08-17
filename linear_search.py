numbers = [x for x in range(10)]

def linear_search(list,target):
    """
        Return the position/index of the target value,else returns None
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None