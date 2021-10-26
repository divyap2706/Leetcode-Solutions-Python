class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #dictionary to map the braces to each other
        charmap = {"}" : "{" , ")" : "(" , "]" : "["}

        for c in s:
            if c in charmap:#we are checking if the given character is a closing brace since in the dictionary all keys are closing braces and their values are opening braces
                if stack and stack[-1] == charmap[c]: #if its a closing brack and stack is not empty, check if the last char in stack(to maintain the order) is the value of c in the dictionary
                    stack.pop() #if yes, pop it
                else:
                    return False
            else:
                stack.append(c)   #if its an opening brace, push it to the stack

        return len(stack) == 0      #return true only if the stack is empty



#Time complexity : O(n)
#Space complexity : O(n) since we are using a stack
