class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # from collections import counter
        table={}
        for word in strs:
            sortedword=sorted(word)
            key=tuple(sortedword)
            if key not in table:
                table[key]=[word]
            else:
                table[key].append(word)
        return list(table.values())

        