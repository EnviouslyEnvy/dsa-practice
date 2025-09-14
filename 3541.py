# Find Most Frequent Vowel and Consonant
class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter
        counted=Counter(s)
        maxv=0
        maxc=0
        for i,n in counted.items():
            if i in "aeiou":
                if n>maxv:
                    maxv=n
            else:
                if n>maxc:
                    maxc=n
        return maxv+maxc
