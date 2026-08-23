class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=len(numbers)-1
        left=0
        # while numbers[left]+numbers[right]!=target:
        while left<right:
            if numbers[left]+numbers[right]<target and left!=len(numbers)-1:
                left+=1
            elif numbers[right]+numbers[left]>target and right!=0:
                right-=1
            else:
                result=[left+1,right+1]
                return result