# space complexity: O(n)
# time complexity: O(n)

# based on solution 1 but cleaner code

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# helper function to make a linked list out of a python list
def makelist(nums: list):
    head = None
    walk = head
    for num in nums:
        node = ListNode(val=num)
        if head is None:
            head = node
            walk = head
        else:
            walk.next = node
            walk = walk.next
    return head

# helper function to print linked list
def printlist(head: ListNode):
    walk = head
    while walk:
        print(walk.val, end=" ")
        walk = walk.next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode() # use a dummy as the first node to avoid edge cases
        walk = dummy
        walk1 = list1
        walk2 = list2

        while walk1 and walk2:
            if walk1.val > walk2.val:
                walk.next = walk2
                walk2 = walk2.next
            else:
                walk.next = walk1
                walk1 = walk1.next
            walk = walk.next
        
        if not walk1:
            walk.next = walk2
        if not walk2:
            walk.next = walk1

        return dummy.next

                

if __name__ == "__main__":
    # list1 = makelist([1, 2, 4])
    # list2 = makelist([1, 3, 4])
    list1 = makelist([0])
    list2 = makelist([])

    solution1 = Solution()
    head = solution1.mergeTwoLists(list1, list2)
    printlist(head)