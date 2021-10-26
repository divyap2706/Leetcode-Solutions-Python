#sliding window optimised approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()  #to avoid duplicates
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
#remove the leftmost char if the current char at right is repeating like "abcabcbb" a is repeating at index 3 so remove a from index 0
                charSet.remove(s[l])
                l += 1     # increase the left pointer
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


#Time complexity : O(n)
#Space complexity : O(n)
