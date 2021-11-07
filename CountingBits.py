class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

#Time complexity : O(n)
# 0 -> 0000 -> 0 -> 0
#1 -> 0001 -> 1 -> 1 + dp(n - 1(2 ^ 0)) -> most significant bit is at 1
#2 -> 0010 -> 1 -> 1 + dp(n - 2(2 ^ 1)) -> most significant bit is at 2
#3 -> 0011 -> 2 -> 1 + dp(n - 2(2 ^ 1))
#4 -> 0100 -> 1 -> 1 + dp(n - 4(2 ^ 2))
#5 -> 0101 -> 2 -> 1 + dp(n - 4(2 ^ 2))
#6 -> 0110 -> 2 -> 1 + dp(n - 4(2 ^ 2))
#7 -> 0111 -> 3 -> 1 + dp(n - 4(2 ^ 2))
#8 -> 1000 -> 1 -> 1 + dp(n - 8(2 ^ 3)) -> most significant bit is at 3

#the offset changes to index when index is power of two
