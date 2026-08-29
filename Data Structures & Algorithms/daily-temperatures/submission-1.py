class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Lets work from the end of the temperatures list.
        # when the temperatures are monotonically decreasing, monotonically increasing from the right-left perspective, then we know the point where it started is the point where it ends and thus the point where all the monotonically increasing indices have their distance reference to.
        # We should add these local maxes to the stack. Whenever a monotonic increase ends we need to add the index of the last point in the monotonic increase to the stack. When there is a point that exceeds the most recent local max we should pop it and make it look at the index of the previous local max if the value there is higher.
        # If at any point the value in a monotonic increase from right to left surpasses the most recent local max we also pop it. And again, add the last point of the monotonic stack. Wait a minute, is this the same as the previous point?
        # If the stack is empty, the distance is 0.
        stack=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            curr_temp=temperatures[i]
            # if not stack:
            #     stack.append(i)
            #     result[i]=0
            # else:
            #     while curr_temp>temperatures[stack[-1]]:
            #         result[i]=stack.pop()-i
            #         stack.append(i)
            #     else:
            #         result[i]=stack[-1]-i
            # 1. Clear out the useless colder days
            while stack and curr_temp >= temperatures[stack[-1]]:
                stack.pop()

            # 2. Read the answer based on what is left
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1] - i

            # 3. Add today to the stack for the past days to check
            stack.append(i)
        return result
                
