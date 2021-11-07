class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2  #finding out whether the last bit is 0 or 1
            n = n >> 1     #right shift by 1
        return res

  #Time Complexity : O(32) since max is a 32-bit integer : O(1)      
