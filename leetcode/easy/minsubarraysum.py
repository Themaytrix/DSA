def minSubArrayLen(target, nums) -> int:
        min_len = len(nums)
        temp_arr = []
        # sort nums
        nums.sort()
        # [1,2,2,3,3,4]
        #  set pointers
        l=0
        
        for r in range(len(nums)):
            print(r)
            res_sum = 0
            while res_sum < target and r<len(nums):
                res_sum += nums[r]
                # print(res_sum)
                r+=1
                if res_sum >= target:
                    temp_arr = nums[l:r+1]
                    print(temp_arr)
            l+=1
            # r+=1
        
        return len(temp_arr)

target = 7
nums = [2,3,1,2,4,3]

minSubArrayLen(target,nums)