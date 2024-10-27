def isIsomrphic(t,s):
    # build a hashmap for s->t and t->s
    mapST = {}
    mapTS = {}
    
    # for the characters in t and s
    
    for c1,c2 in zip(t,s):
        # check if c1 exists in map ST and if c1 already has a value pair
        
        if c1 in mapST and mapST[c1] != c2:
            return False
        
        if c2 in mapTS and mapTS[c2] != c1:
            return False
        
        mapST[c1] = c2
        mapTS[c2] = c1
        
    return True


t = "fol"
s = "bar"


print(isIsomrphic(t,s))
        