class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            target=-nums[i]
            if left==i:
                left+=1
            if right==i:
                right-=1
            while left<right:
                twosum=nums[left]+nums[right]
                if twosum==target:
                    if [nums[left],nums[i],nums[right]] not in result:
                        result.append([nums[left],nums[i],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                elif twosum>target:
                    right-=1
                else:
                    left+=1
        return result
