class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""

        n = len(strs)
        for i in range(n):
            s = s + str(len(strs[i])) + "#" + strs[i]        #encoding the string using length and "#" as a delimiter
            print(s)

        return s


    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i = 0
        while i < len(s):             #initially i will always be the length
            j = i
            while s[j] != "#":
                j += 1              #now j will be at # index
            length = int(s[i : j])   #i will be the length hence [i:j], j will not be included in the slicing
            strs.append(s[j + 1 : j + 1 + length]) #we will append j + 1 till length
            i = j + 1 + length #next number will be after j + 1 + length

        return strs
