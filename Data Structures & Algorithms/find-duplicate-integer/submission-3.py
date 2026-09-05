class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Aim for O(1) space with no array modifications.
        # The critical observation here is that every value is within the range 1 to len(nums)-1, so every value is also a valid index.

        # The range starting from 1 instead of 0 prevents the slow and fast pointer from starting at an equal value and instantly ending.

        slow=0
        fast=0
        slow=nums[slow]
        fast=nums[nums[fast]]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        
        # Now lets retire fast and start another slow pointer from the start. According to floyd's the two slow pointers will meet at the start of the cycle (ie the duped value)
        slow2=0

        while slow!=slow2:
            slow=nums[slow]
            slow2=nums[slow2]
        
        return slow