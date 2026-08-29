class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k=1
        high_k=max(piles)
        while low_k<high_k:
            # we converge when this loop condition is no longer valid.
            k=(high_k+low_k)//2
            hours=0
            for pile_size in piles:
                hours+=pile_size//k
                if pile_size%k!=0:
                    hours+=1
            if hours<=h:
                high_k=k
            elif hours>h:
                low_k=k+1
        
        return (high_k+low_k)//2