def merge(nums1, nums2, m=1, n=1):
    i = m-1
    j = n-1
    k = m+n-1

    while j >= 0:
        if nums2[j] > nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -=1
        print(nums1)
        
    
arr1 = [2,0]
arr2 = [1]

merge(arr1,arr2)
