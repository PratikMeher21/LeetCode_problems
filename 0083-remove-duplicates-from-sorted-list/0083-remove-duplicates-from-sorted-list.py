# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        left=head
        right=head.next

        dummyNode=ListNode(0)
        dummy=dummyNode

        dummy.next=head

        while right:
            if left.val != right.val:
                left.next=right
                left=left.next
            right=right.next
        if not right:
            left.next=None
        return dummy.next
                

        