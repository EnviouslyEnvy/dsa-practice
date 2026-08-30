# 974. Subarray sums divisble by K
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        # If you subtract a number with the same division remainder as what you start with, you get something that is divisible perfectly that has no division remainder.
        # We use prefix sums to find a start and endpoint that achieve this. The start point represents the sum up until the start of the subarray and the endpoint is the end of the subarray.
        # this gives us a subarray that is disible by K.
        # We have to make the count for remainder zero 1 to start. Because a nothing ie a sum of zero is already divisible by K. Making other subarrays with remainder requires some starting point to offset the remainder.
        remainder_count=defaultdict(int)
        remainder_count[0]=1
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            remainder=sum%k
            remainder_count[remainder]+=1
        counts=list(remainder_count.values())
        result=0
        for n in counts:
            # combination/choose 2 formula, start and end.
            result+=n*(n-1)//2
        return result
        
