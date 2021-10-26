#One liner python code:
#  return len(nums) != len(set(nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        return False


#Time complexity : O(n)
#Space complexity : O(n)
