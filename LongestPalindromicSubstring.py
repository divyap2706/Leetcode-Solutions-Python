class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:   #consider each character as the middle character and start comparing characters in the left and right one by one
                if (r - l + 1) > resLen:  #updating the length of the resulting substring
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1


            #even length
            l , r = i, i + 1   #for even number of characters in the string use r = i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
        return res
#Time complexity : O(n * 2)
