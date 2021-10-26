class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and len(nums) > 1:  #if length of the array > 1 it cannot contain duplicates
                count += 1
        if(count > 0):
            return True
        else:
            return False

#Time complexity : O(nlogn)
# Space complexity : O(1) this depends on the sorting technique used. If we use heapsort then space complexity will be O(1)
