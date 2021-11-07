class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
  #finding the last digit of n and logical and it with 1 to find out if it is 1 0r 0
            bit = (n >>i) % 2
            res= res | (bit << (31 - i))
            #we or here since we don't want to change any values in previous digits and left shit to make the last digit in n, first digit in res basically reverse it
        return res

#Time and Space Complexity : O(1)
