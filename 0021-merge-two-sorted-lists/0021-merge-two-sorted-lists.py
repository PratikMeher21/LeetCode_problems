# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy

        left=list1
        right=list2

        while left and right:
            if left.val <= right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            
            tail=tail.next
        if left:
            tail.next=left
        else :
            tail.next=right
        return dummy.next


        