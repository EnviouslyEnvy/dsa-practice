class Solution:
    def sumZero(self, n: int) -> List[int]:
        ints=[]
        if n % 2 == 1:
            ints.append(0)
            n-=1
        for i in range(n//2):
            ints.append(i+1)
            ints.append(-(i+1))
        return ints