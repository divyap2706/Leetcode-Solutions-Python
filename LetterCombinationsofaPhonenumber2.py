class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        if digits=="":
            return []

        number=list(digitToChar[digits[0]])
        for digit in digits[1:]:
            number=[old+new for old in number for new in     list(digitToChar[digit])]
        return number
                    
