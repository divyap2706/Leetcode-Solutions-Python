class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_Max = 1
        curr_Min = 1
        res = max(nums)

        for n in nums:
            if n == 0: #if n = 0 reset the curr_Max and curr_Min to 1 so that product of other subarrays can be calculated without 0
                curr_Max = curr_Min = 1
            temp = n * curr_Max #using temp to store the previous max to calculate the curr_Min after updating the curr_Max
            curr_Max = max(n, n * curr_Max, n * curr_Min)
            curr_Min = min(n, temp, n * curr_Min)
            res = max(res, curr_Max)

        return res

       #Time complexity - O(n)
       #Space complexity - O(1)
