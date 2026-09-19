class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = len(s)-1
        # Since a character can only appear in one substring, we must make it so that the string extends all the way to the last index of any character appearing within it
        # This can bring up a case where in the process of extending for one character we find a new character we must account for.
        from collections import defaultdict
        last_indices=defaultdict(int)
        # Lets first go from the right to find the last indices
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_indices:
                last_indices[s[i]]=i

        partition_end = 0
        start=0
        result=[]
        for i in range(len(s)):
            partition_end=max(partition_end, last_indices[s[i]])
            # when we reach the end of partition_end, we can end the
            if i==partition_end:
                result.append(partition_end-start+1)
                partition_end=0
                start=i+1
        
        return result