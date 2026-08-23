class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # table={}
        # for word in strs:
        #     sortedword=sorted(word)
        #     key=tuple(sortedword)
        #     if key not in table:
        #         table[key]=[word]
        #     else:
        #         table[key].append(word)
        # return list(table.values())

        # Counter key method (faster than sorting)\

        from collections import defaultdict
        table=defaultdict(list)
        for word in strs:
            charcount=[0]*26
            for char in word:
                index=ord('a')-ord(char)
                charcount[index]+=1
            key=tuple(charcount)
            table[key].append(word)
        return list(table.values())