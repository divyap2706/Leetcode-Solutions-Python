class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: #[4,5,6,7,0,1,2] if target is greater than mid which is 6 or smaller than nums[l] i.e 4
                                                            #basically we have to search in the right subarray
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 #search in the left subarrat if target > nums[r] or target < nums[mid]
                else:
                    l = mid + 1
        return -1

        
