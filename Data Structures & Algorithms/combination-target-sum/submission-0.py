class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # i mean... just keep calling the function, reducing the target by the number in the list chosen.
        if target < 2:
            return []
        result = []

        start = 0
        def findSum(start, target, combination):
            nonlocal result

            if target < 0:
                return
            
            if target==0:
                result.append(combination.copy())
                return
            
            else:
                for i in range(start, len(nums)):
                    combination.append(nums[i])
                    findSum(i, target-nums[i], combination)
                    combination.pop()
        
        findSum(start,target,[])
        return result