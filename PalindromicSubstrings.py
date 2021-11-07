class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPalindrome(s, i, i)  #odd length substring
            count += self.countPalindrome(s, i, i + 1)  #even length substring

        return count

    def countPalindrome(self, s, l , r):   #similar to longest Palindromic substring we will use center element and then check if s[l] == s[r]
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            r += 1
            l -= 1
        return count

#Time complexity : O(n * 2)
