class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitToChar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i,currstr):
                if(len(currstr)==len(digits)):
                    res.append(currstr)
                    return res
                for c in digitToChar[digits[i]]:
                    print(i,c,currstr)
                    backtrack(i+1, currstr+c)
        if digits:
            backtrack(0,"")

        return res
