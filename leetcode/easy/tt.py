def findAv(nums,k):
    max_sum = float("-inf")
    curr_sum = 0
    count = 0

    l=0

    for r in range(len(nums)):

        if count <= k:
            curr_sum += nums[r]
            print(curr_sum)
            count+=1

        print(curr_sum)
        while count > k:
            print("here")
            curr_sum -= nums[l]
            print(curr_sum)
            count -= 1
            l+=1
        
        max_sum = max(max_sum,curr_sum)
        # print(max_sum)
    return max_sum / k


nums = [-1]

print(findAv(nums, 1))