class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        ls_products=[0]*len(nums)
        rs_products=[0]*len(nums)
        ls_products[0]=nums[0]
        rs_products[-1]=nums[-1]
        for i in range(len(nums)-1):
            ls_products[i+1]=ls_products[i]*nums[i+1]
        # for i in reversed(range(len(nums)-1)):
        for i in range(len(nums)-2,-1,-1):
            rs_products[i]=rs_products[i+1]*nums[i]
        
        for i in range(len(nums)):
            if i==0:
                output[0]=rs_products[1]
            elif i==len(nums)-1:
                output[-1]=ls_products[-2]
            else:
                output[i]=ls_products[i-1]*rs_products[i+1]
        
        return output