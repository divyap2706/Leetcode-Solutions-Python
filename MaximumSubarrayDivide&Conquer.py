class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findmaxsubarray(nums, left, right):
            curr = 0
            max_left_sum = 0
            max_right_sum = 0

            if(left > right):
                return -math.inf

            mid = left + (right - left) // 2

            for i in range(mid - 1, left - 1, -1):              #calculate the max_sum for left subarray
                curr += nums[i]
                max_left_sum = max(max_left_sum, curr)
                
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                max_right_sum = max(max_right_sum, curr)       #calculate the max_sum for right subarray

            max_combined_sum = nums[mid] + max_left_sum + max_right_sum      #calculate sum of left subarray + mid + right subarray

            left_half = findmaxsubarray(nums, left, mid - 1)        #call recursion for left subarray
            right_half = findmaxsubarray(nums, mid + 1, right)      #call recursion for right subarray

            return max(max_combined_sum, left_half, right_half)       #calculate max sum

        return findmaxsubarray(nums, 0, len(nums) - 1)        #call recursion for the entire nums array
