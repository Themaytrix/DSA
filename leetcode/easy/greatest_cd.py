def gcdOfStrings(str1: str, str2: str) -> str:
        res = ""
        print(len(str2))

        for i in range(len(str2)):
            if str1[i] == str2[i]:
                res += str1[i]
                print(res)
                print(str1[i])
                print(str2[i])
            elif str1[i] != str2[i] or str2[i] in res:
                return res
            
                
                
                
str1 = "ABCABC"
str2 = "ABC"


gcdOfStrings(str1,str2)