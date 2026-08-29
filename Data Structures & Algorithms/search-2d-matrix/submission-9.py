class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start with cols
        left=0
        right=len(matrix)-1
        if right==-1:
            return False
        # while left<right:
        #     mid=(right-left)//2+left
        #     if target==matrix[mid][0]:
        #         return True
        #     elif matrix[mid][0]<target and matrix[mid+1][0]<target:
        #         left=mid+1
        #     elif matrix[mid][0]>target and matrix[mid-1][0]>target:
        #         right=mid-1
        #     elif matrix[mid][0]<target and matrix[mid+1][0]>target:
        #         row=mid
        #         break
        #     elif matrix[mid][0]>target and matrix[mid-1][0]<target:
        #         row=mid-1
        #         break

        # This runs into problem where mid+1 or mid-1 might not exist, like at the top rows and bottom rows.

        while left<=right:
            mid=(right-left)//2+left
            if target==matrix[mid][0]:
                return True
            elif matrix[mid][0]<target and matrix[mid][-1]>=target:
                row=mid
                break
            elif matrix[mid][0]<target:
                left=mid+1
            elif matrix[mid][0]>target:
                right=mid-1

        if left>right:
            return False
        left=0
        right=len(matrix[row])-1
        while left<=right:
            mid=(right-left)//2+left
            if target==matrix[row][mid]:
                return True
            elif matrix[row][mid]<target:
                left=mid+1
            elif matrix[row][mid]>target:
                right=mid-1
        return False