# time complexity: O(2n)
# space complexity: O(n)

# the diameter of a binary tree is the depth of its left subtree plus the depth of the right subtree plus 2
# first traverse the tree in dfs and cache the depth of each subtree in a hashmap
# then dfs the tree again using the hashmap to get the diameter of each subtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        lookup = {}
        self.cache_length_of_subtree(root, lookup)
        max_path = self.walk(root, lookup, 0)
        return max_path
    
    def walk(self, root: TreeNode, lookup: dict, max_path: int) -> int:
        if not root:
            return max_path
        max_path = self.walk(root.left, lookup, max_path)
        max_path = self.walk(root.right, lookup, max_path)
        left = 1 + lookup[root.left] if root.left else 0
        right = 1 + lookup[root.right] if root.right else 0
        path = left + right
        if path > max_path:
            return path
        else:
            return max_path

    def cache_length_of_subtree(self, root: TreeNode, lookup: dict) -> int:
        if not root:
            return 0
        left_len = 1 + self.cache_length_of_subtree(root.left, lookup) if root.left else 0
        right_len = 1 + self.cache_length_of_subtree(root.right, lookup) if root.right else 0
        if left_len > right_len:
            lookup[root] = left_len
            return left_len
        else:
            lookup[root] = right_len
            return right_len
        
        