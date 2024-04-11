# time complexity: O(n)
# space complexity: O(1)

# dfs the tree and everytime dfs goes doen one more level, add one to a varible
# return the maximum of the variable

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = [0]
        def dfs(root: TreeNode, depth: int):
            if not root:
                return
            depth += 1
            if depth > max_depth[0]:
                max_depth[0] = depth
            dfs(root.left, depth)
            dfs(root.right, depth)
        dfs(root, 0)
        return max_depth[0]