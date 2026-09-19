class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # The only operation that can be done is replace the maxes of the current with a new.

        # We want to simply eliminate triplets that won't work
        # If the sum of the triplet is higher than the target, we can ignore it. It must have some value in it that is higher than a targets?
        # But there's more coverage and efficiency in just comparing each triple value to the target.
        # Ex: [4,1,1] vs target [3,3,3] has sum less than the target but can be ruled out due to 4.
        a_check=False
        b_check=False
        c_check=False
        for i in range(len(triplets)):
            a = triplets[i][0]
            b = triplets[i][1]
            c = triplets[i][2]

            if a>target[0]:
                continue
            if b>target[1]:
                continue
            if c>target[2]:
                continue

            if a==target[0]:
                a_check=True
            if b==target[1]:
                b_check=True
            if c==target[2]:
                c_check=True

            if a_check and b_check and c_check:
                return True
        
        return False