class Solution:
    def binary_search(self,left: int,right: int , nums: List[int], target: int) -> int:
        mid=(right-left)//2+left
        if left>right:
            return -1
        elif nums[mid]==target:
            return mid
        elif nums[mid]<target:
            return self.binary_search(mid+1,right,nums,target)
        else:
            return self.binary_search(left,mid-1,nums,target)
    
    
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        return self.binary_search(left,right,nums,target)