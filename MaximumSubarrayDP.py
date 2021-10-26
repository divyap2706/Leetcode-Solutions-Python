class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        curr_subarray = nums[0]
        for i in range(1,len(nums)):
            curr_subarray = max(nums[i] , curr_subarray + nums[i])
            max_subarray = max(max_subarray, curr_subarray)

        return max_subarray

#Time complexity : O(n)
#Space complexity : O(1)

#Dynamic Programming(kadane's Algorithm)           
