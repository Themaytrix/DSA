def reverseWords(s: str) -> str:
    # set trailing pointer and starting
    j =i=0 
    temp = []

    while i < len(s):

        while i<len(s) and s[i] != " ":
            i+=1
        
        temp.append(s[j:i])
        i+=1
        j=i
    
    temp[::-1]
    print(temp)

    return " ".join(temp)



s = "the sky is blue"

reverseWords(s)