class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

#two arrays are already sorted, let's say we have nums1 = [5,6,7,0,0,0] , m = 3, nums2 = [1,2,3] , n = 3.
#We will have the while loop terminated for m and would have n = 3 still with nums1 now [5,6,7,5,6,7] .
#Now, all that nums1[:n] = nums2[:n] does is set the first [:n] numbers as first [:n] of nums2.
#This is because there is a case that there are still elements in nums2 smaller than nums1 and are probably the
#smallest which is why they are left out in the comparison with nums1.
