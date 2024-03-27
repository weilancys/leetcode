# time complexity: O(n)
# space complexity: O(1)

# loop manner
# walks the linked the list, remove the currrent node from it, add it to the reversed linked list, until list end is reached

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        walk = head
        while walk:
            head = walk.next
            walk.next = new_head
            new_head = walk
            walk = head
        return new_head