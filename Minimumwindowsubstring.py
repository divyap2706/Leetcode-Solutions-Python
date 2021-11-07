class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == " ": return " "  #if the string is empty return ""
        countT =  {} #hashmap for characters in string t
        window = {} #hashmap for our sliding window in string s
        for c in t:
            countT[c] = 1 + countT.get(c, 0)    #update hashmap for string t

        have , need = 0, len(countT)
        res, resLen = [-1 , -1], float("infinity")
        l = 0
        for r in range(len(s)):   #update hashmap window as per l,r pointers from string s
            c = s[r]
            window[c] = 1 + window.get(c , 0)

            if c in countT and window[c] == countT[c]:  #if c is needed i.e it is in countT and current count from window = count in countT
                have += 1  #increase the have count

            while have == need:  #update the res/window only when have == need
                #update our result
                if (r - l + 1) < resLen:
                    res = [l , r]
                    resLen = (r - l + 1)
               #pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""  
