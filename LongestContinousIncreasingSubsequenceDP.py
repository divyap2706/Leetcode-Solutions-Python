class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

#time complexity : O(n)
#Space complexity : O(n)
#Dynamic Programming approach