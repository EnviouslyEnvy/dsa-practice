class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # iterate through the list once with sliding window
        # the number of characters you need to replace in a window is equal to the length minus the identical characters
        # keep moving the right index to the right until it 
        # move left index right when the most frequent character requires more than k replacements (length-most frequent count>k)
        # obviously when we move right we increment the right's count in the counter by 1, when we move left we take the left character and decrease its count by one prior to moving.
        from collections import defaultdict
        counter=defaultdict(int)
        left=0
        right=0
        s=list(s)
        max_length=0
        max_freq=0
        while right<len(s):
            right_char=s[right]
            left_char=s[left]
            counter[s[right]]+=1
            max_freq=max(max_freq,counter[s[right]])
            if (right-left+1)-max_freq>k:
                counter[s[left]]-=1
                left+=1
            else:
                max_length=max(right-left+1, max_length)
            right+=1
        return max_length
