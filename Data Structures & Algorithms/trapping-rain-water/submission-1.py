class Solution:
    def trap(self, height: List[int]) -> int:
        # lets analyze how to think about the water that can be contained.
        # between one height and another, at least one space apart, the water contained is (min(two heights))*(distance between two heights)-heights between them).
        # To keep things optimized, we just subtract the heights between from the global amount.
        # How do we tell if we have a pool with two pointers?
        # Use the last problem's principal. Move the pointer inwards if it's the shorter of the two. If there's a tie then move one or both i suppose? Just handle this case with else statement i guess
        # When we move the pointer inwards, we should keep track of the height we started moving in from. again subtract heights that are shorter.

        left=0
        right=len(height)-1
        left_local_max=0
        right_local_max=0
        vol=0
        while left<right:
            # bottleneck is determined by the lower of the two heights

            if height[left]<height[right]:
                if height[left]>left_local_max:
                    left_local_max=height[left]
                else:
                    vol+=left_local_max-height[left]
                left+=1
            else:
                if height[right]>right_local_max:
                    right_local_max=height[right]
                else:
                    vol+=right_local_max-height[right]
                right-=1
        return vol