class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    //[amount + 1] basically has to be a max value, it can integer.max also
    // we are creating amount + 1 times because we have to calculate from 0 to n
        dp = [amount + 1]  * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    //this means dp[7] = min(dp[7] , 1 + dp[7 - 4])
        //if coin = 4 and a = 7, 1 + because we already have one coin from c in the for loop

        return dp[amount] if dp[amount] != amount + 1 else -1


#Time complexity : O(amount * len(coins))
#Space complexity: O(amount)
#DP bottom up approach
