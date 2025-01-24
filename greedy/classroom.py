def strStr( haystack: str, needle: str) -> int:
    l,r = 0,0
    n = len(haystack)
    s = len(needle)
    

    while l < n:
        r = l + s 
        print(haystack[l:r])
        if r<=n and haystack[l:r] == needle:
            
            return l
        l +=1
    return -1

haystack = "s"
needle = "s"

print(strStr(haystack,needle))
print(((1) % 10))
