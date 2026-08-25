class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # I will use a counter to first count the characters in s1.
        # I will have the right pointer move right, and if a character has a value in the original counter appears does it can decrement it.
        # The left pointer moves at the same speed as right and adds back the value the right decrements as it leaves the subarray length.
        # Aim for zero across all counts.
        # I could also just do a count of s1, store that and compare it to a count for s2 and avoid working on top of the s1 count. Then instead looking for all zeroes it should be just checking for equality. Verifying all zeroes does require extra iteration across values so i think this is a bit easier.
        # I'm not sure if I should use counter, defaultdict, or just an array with ord().
        left=0
        right=0
        char_counts1=[0]*26
        char_counts2=[0]*26
        if len(s1)>len(s2):
            return False
        for char in s1:
            i=ord(char)-ord('a')
            j=ord(s2[right])-ord('a')
            char_counts1[i]+=1
            char_counts2[j]+=1
            right+=1
        if char_counts1==char_counts2:
            return True
        while right<len(s2):
            i=ord(s2[right])-ord('a')
            char_counts2[i]+=1
            if right>=len(s1):
                i=ord(s2[left])-ord('a')
                char_counts2[i]-=1
                left+=1
            if char_counts2==char_counts1:
                return True
            right+=1
        return False