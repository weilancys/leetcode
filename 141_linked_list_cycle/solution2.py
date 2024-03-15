# time complexity: O(n2)
# space complexity: O(1)

# this approach doesn't use any extra memory but is less efficient than the first approach time wise
# it calculates the difference between the current node and its next node while traversing the whole list
# if any of the differences is not 1, the list must have a cycle in it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        walk = head
        while walk and walk.next:
            if self.distance(head, walk.next) - self.distance(head, walk) != 1:
                return True
            walk = walk.next
        return False
    
    def distance(self, head: ListNode, node: ListNode):
        counter = -1
        walk = head
        while walk:
            counter += 1
            if walk == node:
                break
            walk = walk.next
        return counter

        