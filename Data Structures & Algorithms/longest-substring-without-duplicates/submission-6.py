class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        
        seen = set()
        result = 0
        while right < len(s):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            result = max(result, right - left)
            seen.add(s[right])
            right += 1
        return result+1