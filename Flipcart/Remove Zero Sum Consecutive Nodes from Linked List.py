# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        sum=0
        d={0:dummy}
        while head:
            sum+=head.val
            d[sum]=head
            head=head.next
        head=dummy
        sum=0
        while head:
            sum+=head.val
            head.next=d[sum].next
            head=head.next
        return dummy.next
