class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        n=len(s)
        res=0
        l=0
        for r in range(n):
            while s[r] in substr:
                substr.remove(s[l]) #removing the left char because duplicate found in the right
                l+=1
            substr.add(s[r])  #adding the right char
            res=max(res, r - l + 1)
        return res

        return len(substr)
