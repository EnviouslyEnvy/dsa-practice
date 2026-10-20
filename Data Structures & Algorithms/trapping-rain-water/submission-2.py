class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        
        max_lh = max_rh = 0

        # When you move a pointer, add volume = current height 
        
        while left < right:
            lh = height[left]
            rh = height[right]
            max_lh = max(max_lh, lh)
            max_rh = max(max_rh, rh)
            if lh<rh:
                left += 1
                result += max(min(max_lh, max_rh) - height[left], 0)
            else:
                right -= 1
                result += max(min(max_lh, max_rh) - height[right], 0)
        return result