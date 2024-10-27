from collections import defaultdict
def groupanagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for s in strings:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord("a")] += 1

            
        key = tuple(count)
        anagram_dict[key].append(s)
        print(anagram_dict)
    return anagram_dict.values()
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupanagrams(strs))