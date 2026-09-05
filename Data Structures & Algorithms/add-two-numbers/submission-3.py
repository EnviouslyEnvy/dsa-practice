# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # I don't think we can assume the two numbers have the same number of digits.

        head=None
        prev=None
        carry=0
        while l1 and l2:
            curr=ListNode()
            sum=l1.val+l2.val+carry
            if sum>=10:
                carry=1
                digit_sum=sum%10
            else:
                carry=0
                digit_sum=sum
            
            curr.val=digit_sum
            if prev:
                prev.next=curr
            else:
                head=curr
            prev=curr
            l1=l1.next
            l2=l2.next
        
        while l1:
            curr=ListNode()
            sum=l1.val+carry
            if sum==10: # there is leftover carry and the next node is 9.
                carry=1
                digit_sum=0
            else:
                carry=0
                digit_sum=sum
            curr.val=digit_sum
            if prev:
                prev.next=curr
            else:
                head=curr
            prev=curr
            l1=l1.next
            
        while l2:
            curr=ListNode()
            sum=l2.val+carry
            if sum==10: # there is leftover carry and the next node is 9.
                carry=1
                digit_sum=0
            else:
                carry=0
                digit_sum=sum
            curr.val=digit_sum
            if prev:
                prev.next=curr
            else:
                head=curr
            prev=curr
            l2=l2.next
            

        if l1==None and l2==None and carry:
            curr=ListNode(carry)
            carry=0
            prev.next=curr
        
        return head