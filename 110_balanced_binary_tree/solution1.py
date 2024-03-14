# this is the naive approach
# it calculates the depth of two subtrees of each node in a dfs manner and compare the depths to detemine if the tree is balanced

# time complexity: O(n2)
# space complexity: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        return True

    def depth(self, root: TreeNode, level:int=0) -> int:
        if not root:
            return level - 1
        return max(self.depth(root.left, level+1), self.depth(root.right, level+1))