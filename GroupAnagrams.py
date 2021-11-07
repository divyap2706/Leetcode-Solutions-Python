class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #we have used a defaultdict so that we don't get keyerror, default value is provided even if the key doesn't exist in the dictionary
        #list because return type is a list
        for s in strs:
            count = [0] * 26 #a-z initialize for every char to 0
            for c in s:
                count[ord(c) - ord ("a")] += 1 #ord(c) gives ASCII val of the char, subtracting it from ord("a") will map it to the correct index between 0 to 25.
                #for eg: ord("a") = 80
                #ord("b") = 81
                #ord("b") - ord("a") = 1 which is the correct mapping for b between 0 to 25

            res[tuple(count)].append(s) #we are appending the string s as value for key count. count is written as a tuple as list cannot be a key for dictionaries

        return res.values() #lastly since we have to written only the groups, we return the values

#Time complexity : O(n * m) where m is number of strings in the strs and n is the length of each string in strs
