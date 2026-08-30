class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if right==0:
            if nums[0]==target:
                return 0
            else:
                return -1
        
        while left<=right:
            mid=(right+left)//2
            if nums[mid-1]>nums[mid]:
                break
            # If target is contained within the right set
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid-1
        pivot=mid


        if nums[pivot]==target:
            return pivot
        if pivot < len(nums) - 1 and target >= nums[pivot + 1] and target <= nums[-1]:
            left=pivot+1
            right=len(nums)-1
            while left<=right:
                mid=(right+left)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        
        else:
            left=0
            right=pivot-1
            while left<=right:
                mid=(right+left)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        return -1