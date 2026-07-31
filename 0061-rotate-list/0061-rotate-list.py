# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        #calculate the length of the list
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        
        k=k%length

        if k == 0:
            return head

        left=head
        right=head

        for _ in range(k):
            right=right.next

        while right.next :
            right=right.next
            left=left.next

        newhead=left.next

        left.next=None
        right.next=head

        return newhead

                