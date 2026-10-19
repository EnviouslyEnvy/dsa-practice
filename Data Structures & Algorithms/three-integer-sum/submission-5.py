class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        result = []

        while i<len(nums):
            target = nums[i]
            if i and nums[i-1]==target:
                i += 1
            
            else:
                left = i+1
                right = len(nums)-1
                

                while left < right:
                    left_val, right_val = nums[left], nums[right]
                    if left!=i+1 and left_val == nums[left-1]:
                        left+=1
                        continue
                    if right != len(nums)-1 and right_val == nums[right+1]:
                        right-=1
                        continue
                    
                    if left_val + right_val < -target:
                        left += 1
                    elif left_val + right_val > -target:
                        right -= 1
                    else:
                        result.append([target, left_val, right_val])
                        left += 1
                        # DON'T FORGET TO MOVE EVEN AFTER FINDING A WORKING TRIPLE OTHERWISE STUCK HERE AND TLE
                i += 1
        
        return result