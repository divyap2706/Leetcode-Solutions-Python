class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1 , -1):  #going from the last element to first element  
            for j in range(i + 1, len(nums)):  
                if nums[i] < nums[j]: #if the next element is > than the current element
                    LIS[i] = max(LIS[i], 1 + LIS[j]) #only then LIS will be updated for i, 1 + LIS[j] is like count(num) at i which is one + LIS[j] that is increasing subsequence at j
        return max(LIS)
    


    #Time complexity : O(n ^ 2)
    #Space complexity : O(n)
    