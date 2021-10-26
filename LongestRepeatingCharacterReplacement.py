class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #adds 1 to count of s[r] if it exists in the hashmap otherwise default value 0

            while (r - l + 1) - max(count.values()) > k:#we are using this condition to find out how many replacements we can,
            #we will replace the characters that are least frequent
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

#the basic idea here is to use hashmap to store count of all elements and sliding window to find if the length of the substring - max value of a character in
the substring > k(number of times we can replace), if yes then we increment the left counter. We don't actually replace any characters in the string just
count the number of replacements we can make

#Time Complexity : O(26n) -> O(n) (26n to find max value of all characters from the hashmap count in the while value)
            
