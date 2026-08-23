class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups=defaultdict(list)
        for word in strs:
            char_counts=[0]*26
            for char in word:
                char_counts[ord('a')-ord(char)]+=1
            groups[tuple(char_counts)].append(word)
        return list(groups.values())