class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counted=Counter(nums)
        counted=counted.most_common(k)
        result=[]
        for i in counted:
            result.append(i[0])
        return result
        # [(key,3), (key,3)]
        # max_freq=counted[0][1]
        # result=[]
        # for i in counted:
        #     if i[1]<max_freq:
        #         return result
        #     else:
        #         result.append(i[0],max)
        # return result