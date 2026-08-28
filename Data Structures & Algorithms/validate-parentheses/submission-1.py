class Solution:
    def isValid(self, s: str) -> bool:
        brackets={'}':'{',']':'[',')':'('}
        openingbrackets={'{','[','('}
        stack=[]
        for char in s:
            if char in openingbrackets:
                stack.append(char)
            else:
                if stack==[]:
                    return False
                elif char in brackets and brackets[char]!=stack.pop():
                    return False
        if stack==[]:
            return True 
        else:
            return False