class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # counted=Counter(nums)
        # counted=counted.most_common(k)
        # result=[]
        # for i in counted:
        #     result.append(i[0])
        # return result

        from collections import defaultdict
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        numfreqs=[]
        for num in count:
            numfreqs.append((count[num],num))
        numfreqs.sort()
        numfreqs=numfreqs[::-1]
        result=[]
        for i in range(k):
            result.append(numfreqs[i][1])
        return result