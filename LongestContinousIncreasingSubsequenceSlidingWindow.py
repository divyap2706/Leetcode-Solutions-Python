class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if nums[i - 1] >= nums[i]:
                anchor = i              #anchor is updated every new subarray where i + 1 is < i
            ans = max(ans, i - anchor + 1)
        return ans


#Time complexity : O(n)
#Space complexity : O(1)
#Sliding window approach