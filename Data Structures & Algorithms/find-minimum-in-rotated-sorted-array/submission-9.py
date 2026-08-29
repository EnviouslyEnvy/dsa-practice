class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Use binary search:
        # If right side of a split is greater than the left, we know the min is in the other partition or its the left side.
        # If the left side is greater than right we know the reset (and thus min) is in there

        left=0
        right=len(nums)-1
        mid=(right+left)//2
        if right==0:
            return nums[0]
        while left<=right:
            mid=(right+left)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]>nums[right]:
                left=mid+1
            # elif nums[mid]<nums[right]:
            #     # The opposite of this is that the the left value of the right partition is greater than the right, implying the reset happens in that partition.
            #     right=mid-1
            else:
                right=mid-1
        
        