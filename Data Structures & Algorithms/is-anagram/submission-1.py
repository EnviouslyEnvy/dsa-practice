class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s = Counter(s)
        t = Counter(t)
        if s==t:
            return True
        return False
        