class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permute_rem(nums, curr_list):
            # nonlocal result
            
            if not nums:
                result.append(curr_list.copy())
            
            for i in range(len(nums)):
                nums_copy = nums.copy()
                temp = nums_copy.pop(i)
                # removes num, on next iteration number should be added back
                curr_list.append(temp)
                permute_rem(nums_copy,curr_list)
                curr_list.pop()
                # nums.append(temp)
        result = []
        
        permute_rem(nums, [])
        return result