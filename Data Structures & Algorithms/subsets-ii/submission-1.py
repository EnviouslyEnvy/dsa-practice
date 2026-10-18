class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # We can sort the list. skip over adding a number if it is the same as the last one.
        # We never want to look "backwards in the list"
        nums.sort()
        result = []
        length = len(nums)
        def backtrack(curr, start):
            result.append(curr.copy())
            # Always do this, empty set counts so it's ok to do this first
            for i in range(start, length):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()
                
            
        backtrack([], 0)

        return result