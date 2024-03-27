# time complexity: O(n)
# space complexity: O(n)

# recursive manner
# pretty much identical logic to the loop manner, but traversing the list with the recursive manner instead

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
    
    def walk(self, head: ListNode, new_head: ListNode):
        if not head:
            return new_head
        next = head.next
        head.next = new_head
        new_head = head
        return self.walk(next, new_head)