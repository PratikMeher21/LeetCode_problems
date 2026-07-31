# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        # Move to the left position
        pos = 1
        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1

        beforeLeft = prev
        leftNode = curr

        # Dummy list for reversed part
        revDummy = ListNode(0)

        while pos <= right:
            nxt = curr.next

            # Insert current node at front of revDummy
            curr.next = revDummy.next
            revDummy.next = curr

            curr = nxt
            pos += 1

        # Connect the reversed part
        beforeLeft.next = revDummy.next
        leftNode.next = curr

        return dummy.next
        
            
        