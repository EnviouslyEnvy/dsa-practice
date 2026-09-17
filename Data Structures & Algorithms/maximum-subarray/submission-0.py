class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=float('-inf')
        maxSum=float('-inf')
        for num in nums:
            if num>curSum+num:
                curSum=num
            else:
                curSum+=num
            maxSum=max(curSum,maxSum)
        
        return maxSum