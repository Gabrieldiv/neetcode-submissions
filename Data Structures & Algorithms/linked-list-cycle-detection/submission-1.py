# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lebre, tartaruga = head, head

        while lebre and lebre.next:
            tartaruga = tartaruga.next
            lebre = lebre.next.next
            if tartaruga == lebre:
                return True

        return False
        