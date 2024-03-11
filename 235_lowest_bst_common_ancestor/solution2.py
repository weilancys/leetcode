# time complexity: O(logn)
# space complexity: O(1)

# traverse down the bst while comparing the value of p, q and current
# if p and q are on the same side of the tree, traverse down to the side where q and q reside
# repeat until a split between p and q is found
# that split is the LCA of p and q

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current
        return current