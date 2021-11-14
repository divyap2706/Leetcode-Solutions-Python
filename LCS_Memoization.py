from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize = None)
        def memo_lcs(p1, p2):
            #if either of the string is now empty, we can't match the characters anymore
            if(p1 == len(text1) or p2 == len(text2)):
                return 0
            
            #if chars match, add 1 to length and call the function for next two chars in both strings
            if(text1[p1] == text2[p2]):
                return 1 + memo_lcs(p1 + 1, p2 + 1)
            
        #if chars don't match, store max of either dropping one char form first string or one char from the second string   
        else:
                return max(memo_lcs(p1, p2 + 1), memo_lcs(p1 + 1, p2))
            
        return memo_lcs(0, 0)
    
#Time complexity : O(m * n), time taken to solve each subproblem is O(1)
#Space complexity : O(m * n), we need to store answer for each subproblem and there are m * n subproblems
#Memoization approach