class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[]
        t=""
        for i in s:
            if i in "AEIOUaeiou":
                vowels.append(i)
        vowels.sort()
        for i in s:
            if i in "AEIOUaeiou":
                t+=vowels.pop(0)
            else:
                t+=i
        return t
        # This solution is slow.