# space complexity: O(n)
# time complexity: O(n)

# this is the basic approach to solve the problem
# just iterate through the two linked list at the same time
# then compare each leftmost element and add the smallest one to the new linked list, update the pointer accordingly
# when one list is exhausted, add the remaining part of the other list to the end of the new list

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
    while walk is not None:
        print(walk.val, end=" ")
        walk = walk.next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None

        head = None
        walk = head
        walk1 = list1
        walk2 = list2

        while walk1 is not None and walk2 is not None:
            if walk1.val < walk2.val:
                new_node = ListNode(walk1.val)
                if head is None:
                    head = new_node
                    walk = head
                else:
                    walk.next = new_node
                    walk = walk.next
                walk1 = walk1.next
            elif walk1.val > walk2.val:
                new_node = ListNode(walk2.val)
                if head is None:
                    head = new_node
                    walk = head
                else:
                    walk.next = new_node
                    walk = walk.next
                walk2 = walk2.next
            else:
                new_node_1 = ListNode(walk1.val)
                new_node_2 = ListNode(walk2.val)
                if head is None:
                    head = new_node_1
                    new_node_1.next = new_node_2
                    walk = new_node_2
                else:
                    walk.next = new_node_1
                    new_node_1.next = new_node_2
                    walk = new_node_2
                walk1 = walk1.next
                walk2 = walk2.next
        
        if walk1 is None:
            walk.next = walk2
        elif walk2 is None:
            walk.next = walk1

        return head
                

if __name__ == "__main__":
    # list1 = makelist([1, 2, 4])
    # list2 = makelist([1, 3, 4])
    list1 = makelist([])
    list2 = makelist([0])

    solution1 = Solution()
    head = solution1.mergeTwoLists(list1, list2)
    printlist(head)