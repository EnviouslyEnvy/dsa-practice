class Solution:
    def jump(self, nums: List[int]) -> int:
        # Same in concept, but now we must return the minimum number of jumps.
        l = r = 0
        # upon next iteration update l to r+1 and r becomes the furthest reachable index from the range from current l + r. Perhaps this can be found while moving l to r+1
        # The result is the number of times this iteration occurs.
        count=0
        while r<len(nums)-1:
            l_new=r+1
            r_new=l_new
            while l<l_new:
                r_new=min(max(l+nums[l],r_new),len(nums)-1)
                l+=1
            r=r_new
            count+=1
        return count