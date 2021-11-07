class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}

        for c in s:
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1

        for c in t:
            if c in dictionary:
                dictionary[c] -= 1
            else:
                return False

        for val in dictionary.values():
            if val != 0:
                return False

        return True
