class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=n//2
        b=n//2+n%2
        while ("0" in str(a)) or ("0" in str(b)):
            a=a-1
            b=b+1
        return[a,b]