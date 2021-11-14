class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #creating a 2d matrix with extra 0s row and column for ease
        dp_grid = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        #Iterate up each column, starting from the last one 
        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
            
        return dp_grid[0][0]    #this is the orignal problem   

#Time complexity : O(m * n), time taken to solve each subproblem is O(1)
#Space complexity : O(m * n), we need to store answer for each subproblem and there are m * n subproblems
#Dynamic Programming approach