# time complexity: O(n)
# space complexity: O(1)

# traverse the list and get the length
# middle index is length divided by 2
# traverse the list again and when index hits middle, return the current node

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        idx = -1
        walk = head
        while walk:
            idx += 1
            walk = walk.next
        mid = (idx + 1) // 2
        idx = -1
        walk = head
        while walk:
            idx += 1
            if idx == mid:
                return walk
            walk = walk.next
        return None
        