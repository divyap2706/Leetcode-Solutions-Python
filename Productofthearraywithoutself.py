class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix           #assigning the prefix to the current result array
            prefix *= nums[i]         #updating the prefix with every number

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix         #multiplying the prefix array with postfix
            postfix *= nums[i]        #calculating the postfix of every number

        return res


  #Time complexity : O(n)
  #Space complexity : O(1)
