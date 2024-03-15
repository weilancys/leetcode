# time complexity: O(n)
# space complexity: O(n)

# keep track of every visited node in a set and keep traversing the linked list
# if the current node is not in the set, add it to the set
# if its in the set already, it is a linked list with a cycle in it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set() # set is implemented as a hashmap in python, which is O(1) in lookup, better than list, which is implemented as an array and has O(n) lookup time
        walk = head
        while walk:
            if walk not in visited:
                visited.add(walk)
            else:
                return True
            walk = walk.next
        return False