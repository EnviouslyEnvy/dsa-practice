class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # move right substring until duplicate character appears.
        # then move the left until you advance past the character the right now sees. still track when the right pointer last saw that character with a dict?
        # constantly save length and track max
        left=0
        max_length=0
        right=0
        seen={}
        s=list(s)
        while right<len(s):
            rightChar=s[right]
            if rightChar not in seen:
                seen[rightChar]=right
            elif rightChar in seen:
                left=max(left,seen[rightChar]+1)
                seen[rightChar]=right
            max_length=max(max_length,right-left+1)
            right+=1
        return max_length

        # seen={}
        # s=list(s)
        # max_length=0
        # for i in range(len(s)):
        #     if s[i] not in seen:
        #         seen[s[i]]=i
        #     else:
        #         if i-seen[s[i]]>max_length:
        #             max_length=i-seen[s[i]]
        #         seen[s[i]]=i
        # return max_length