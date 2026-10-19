class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            l_num = numbers[left]
            r_num = numbers[right]

            if l_num + r_num < target:
                left += 1
            elif l_num + r_num > target:
                right -= 1
            else:
                return [left + 1, right + 1]