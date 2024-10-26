def canconstruct(ransomnote,magazine):
    # construct hashmap of counter
    counter = {}
    
    for c in magazine:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
            
    for c in ransomnote:
        if c not in magazine or counter[c] < 1:
            return False
        else:
            counter[c] -= 1
    
    return True
            
   
    

ransomnote = "aa"
magazine = "b"

print(canconstruct(ransomnote,magazine))