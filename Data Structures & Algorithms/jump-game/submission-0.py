class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # We can work backwards.
        # Calculate each index as having a route to the end or not.
        goal = len(nums)-1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                # Can we reach the goal?
                goal = i
                # If we can a new goal is now i.
        
        if goal == 0:
            return True

        else:
            return False