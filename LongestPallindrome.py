class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)     #every character is first added in the set and then removed if it's pair is found. In the end there are only unpaired characters in the set.
                #print("if")
                #print(ss)
            else:
                ss.remove(letter)
                #print("else")
                #print(ss)
        #print(len(ss))
        if len(ss) != 0:     #in the end if the length of the set is not 0, meaning there are odd number of characters in the string so 1 is added for center character
        #if all characters are different like abcde, the length of the longestPalindrome will be 1.
            return len(s) - len(ss) + 1
        else:
            return len(s)    #for even length strings

#time complexity : O(n)
Space complexity: O(n)
