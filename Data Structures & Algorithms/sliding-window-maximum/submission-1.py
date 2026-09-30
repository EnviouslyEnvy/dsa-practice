class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # NOT A GREAT SOLUTION, I TRACK MAX VALUES USING TWO VARIABLES WHEN I CAN JUST PEEK AT LEFT OF DQ
        result=[]
        left = 0
        right = k-1
        max_val = - 10001
        from collections import deque
        dq = deque()
        dq.append((nums[0], 0))
        for i in range(1, k):
            # max_val = max(max_val, nums[i])
            # max_index = i
            if nums[i]<dq[0][0]:
                dq.appendleft((nums[i], i))
            else:
                while dq and nums[i]>dq[0][0]:
                    dq.popleft()
                    continue
                dq.appendleft((nums[i],i))
        
        if dq:
            max_val, max_index = dq.pop()
        result.append(max_val)
                    
        left+=1
        right+=1


        while right < len(nums):

            
            
            while dq and nums[right]>dq[0][0]:
                dq.popleft()
            dq.appendleft((nums[right],right))
            
            if max_index<left or max_val<dq[-1][0]:
                max_val, max_index = dq.pop()
                while max_index<left:
                    max_val, max_index = dq.pop()

            result.append(max_val)

            left+=1
            right+=1
        return result
            # should probably think of a more clever way of tracking the maximum rather than literally taking max of the 3 elements each step...
            