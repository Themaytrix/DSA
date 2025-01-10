def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"

    # define pointers
    slist = list(s)

    l, r = 0, len(slist) - 1

    while l < r:
        while slist[l] not in vowels:
            l += 1
        print(slist[l])
        while slist[r] not in vowels:
            r -= 1
        print(slist[r])
        # swap
        slist[l], slist[r] = slist[r], slist[l]

        r -= 1
        l += 1
    return "".join(slist)


s = "leetcode"

reverseVowels(s)
