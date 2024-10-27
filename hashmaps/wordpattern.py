def wordPattern(pattern: str, s: str) -> bool:
        wordmap = {}
        word = split(s)

        for c,w in zip(pattern,word):
            
            if c in wordmap and wordmap[c] != w:
                print("here")
                return False
            wordmap[c] = w
            
        return True
    
pattern = "abba"
word = "dog cat cat dog"

def split(s):
    words = []
    word = ""
    
    for c in s:
        # check if character is a space
        if c == " ":
            # check if word is valid
            if word:
                words.append(word)
                # reset word
                word = ""
            print(words)
        else:
            # form word
            word += c
    # if no more space. append the rest as a word
    if word:
        words.append(word)
    
    return words

print(wordPattern(pattern,word))

# print(split(word))