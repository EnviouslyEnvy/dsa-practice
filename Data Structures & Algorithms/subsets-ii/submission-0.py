class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # We can sort the list. skip over adding a number if it is the same as the last one.
        # We never want to look "backwards in the list"
        nums.sort()
        result = []
        length = len(nums)
        def backtrack(i, curr):
            if i == len(nums):
                result.append(curr.copy())
                return
            
            # for i in range(start+1, length):
            #     backtrack(nums, curr, start)

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            backtrack(i + 1, curr)

        backtrack(0, [])

        return result