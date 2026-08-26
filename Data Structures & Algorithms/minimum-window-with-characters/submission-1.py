class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        right=0
        # it seems like this is case sensitive given the last constraint
        # it seems like the duplicate clause implies that if the substring has multiple of a character the substring must include the same amount.
        # lets use an array of characters using []*52 ord('a')-ord(s[i])
        # move the right until the end
        # initially move the left to where the the right encounters its first character in t
        # when right encounters a character that causes the count to go above the target count in t, and that character is the same as the one the left is stuck on, the left should move until it reaches another required character.
        # i don't think this is specifically how left movement should be triggered. It should continually try to move left unless it's on a character where the count of it in the window is lower than the count of it in t.

        t=list(t)
        s=list(s)
        from collections import Counter
        from collections import defaultdict
        
        # target_counts=Counter(t)
        counter_t=defaultdict(int)
        counter_window=defaultdict(int)
        for char in t:
            counter_t[char]+=1
        shortest_length=float('inf')
        # only keep track of how many character counts are satisfied
        satisfied=0
        need=len(counter_t)
        while right<len(s):
            counter_window[s[right]]+=1
            if counter_window[s[right]]==counter_t[s[right]]:
                satisfied+=1
            while left<len(s) and counter_t[s[left]]<counter_window[s[left]]:
                counter_window[s[left]]-=1
                left+=1
            
            if satisfied==need and right-left<shortest_length:
                shortest_length=right-left
                interval=[left,right]
            right+=1
        if satisfied!=need:
            return ''
        substring=s[interval[0]:interval[1]+1]
        substring=''.join(substring)
        return substring