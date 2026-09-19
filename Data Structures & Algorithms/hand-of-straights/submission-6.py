
        # Ok when we first encounter a number we know that the groupSize-1 next numbers must have the same count or more.
        # So five ones must mean at least 5x 2, 3, 4, if groupSize=4. If two has 6, then we need to expect 6-5=1 more of 3, 4, 5.
        # We can see if the counts are correct in this way. We subtract expected count of a number from the future numbers if it has been over groupSize numbers...
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        from collections import Counter
        from collections import deque

        counts = Counter(hand)
        unique_nums = sorted(counts.keys())

        queue = deque()
        active_requirement_sum = 0
        prev = None

        for num in unique_nums:

            # If there's a gap while groups are still unfinished
            if prev is not None and num != prev + 1:
                if active_requirement_sum > 0:
                    return False

            # Current number must satisfy all currently active groups
            new_requirement = counts[num] - active_requirement_sum

            if new_requirement < 0:
                return False

            # Start new groups with the extra copies of num
            queue.append(new_requirement)
            active_requirement_sum += new_requirement

            # Groups started groupSize numbers ago are now complete
            if len(queue) == groupSize:
                active_requirement_sum -= queue.popleft()

            prev = num

        return active_requirement_sum == 0

# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand)%groupSize!=0:
#             return False

#         from collections import Counter
#         from collections import deque

#         counts=Counter(hand)
#         unique_nums=sorted(counts.keys())
#         queue = deque()
#         active_requirement_sum=0
#         for i in range(len(unique_nums)):
#             num=unique_nums[i]

#             # Remove groups that have already finished
#             if queue and i>=queue[0][0]:
#                 active_requirement_sum-=queue.popleft()[1]

#             # If there is a gap that is greater than 1 while a group still needs sequential numbers.
#             if i > 0 and num != unique_nums[i - 1] + 1:
#                 if active_requirement_sum > 0:
#                     return False

#             new_requirement = counts[num] - active_requirement_sum

#             if new_requirement > 0:
#                 queue.append((i+groupSize, new_requirement))
#                 active_requirement_sum += new_requirement
            
#             if new_requirement < 0:
#                 return False
        
#         while queue and len(unique_nums) >= queue[0][0]:
#             active_requirement_sum -= queue.popleft()[1]

#         return active_requirement_sum == 0



            