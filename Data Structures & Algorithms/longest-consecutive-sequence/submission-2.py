class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # max_length=0
        # current_length=0
        # if nums==[]:
        #     return 0
        # for i in range(len(nums)):
        #     if i==0:
        #         current_length=1
        #         max_length=1
        #     elif nums[i]==nums[i-1]+1:
        #         current_length+=1
        #         max_length=max(current_length,max_length)
        #     else:
        #         current_length=1
        # return max_length

        # Ok so this solves another problem entirely my bad..
        current_length=0
        max_length=0
        nums_set=set(nums)
        for num in nums_set:
            current_length=1
            max_length=max(max_length,1)
            if num-1 in nums_set:
                continue
            else:
                while num+1 in nums_set:
                    current_length+=1
                    max_length=max(current_length,max_length)
                    num+=1
    
        return max_length