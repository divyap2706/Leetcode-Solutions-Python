#solution self
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,len(nums) + 1):
            if i in nums:
                continue
            else:
                return i

  #solution 2 - XOR
  class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        for num in nums:
            res ^= num
        return res


  #solution 3 - sum
  class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
            print(res)
        return res
