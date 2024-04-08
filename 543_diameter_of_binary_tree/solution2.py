# time complexity: O(n)
# space complexity: O(1)

# dfs the tree, return the height of the subtree in each iteration
# during dfs, when the diameter of current subtree is larger than the current record, update current record

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_path = [0]
        def dfs(root: TreeNode) -> int:
            if not root:
                return -1 # height of null tree is -1 to facilitate the math
            left = dfs(root.left)
            right = dfs(root.right)
            path = 1 + 1 + left + right
            if path > max_path[0]:
                max_path[0] = path
            return max(1 + left, 1 + right)
        dfs(root)
        return max_path[0]
        
        