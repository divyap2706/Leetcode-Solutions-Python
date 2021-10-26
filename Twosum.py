class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hashmap:
                return[hashmap[y], i]
            hashmap[nums[i]] = i   #written this at last to avoid duplicate values like in [3,2,4] and  target 6 so the program wont return 0,0
