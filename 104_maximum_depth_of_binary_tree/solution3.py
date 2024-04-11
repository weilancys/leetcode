# time complexity: O(n)
# space complexity: O(n)

# bfs the tree, count the children nodes in each iteration, and plus one everytime bfs goes down a level

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = []
        if root:
            queue.append(root)
        level = 0
        children_count = 1
        while queue:
            count = 0
            for i in range(children_count):
                item = queue.pop(0)
                if item.left:
                    queue.append(item.left)
                    count += 1
                if item.right:
                    queue.append(item.right)
                    count += 1
            children_count = count
            level += 1
        return level
    
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode()
    res = solution.maxDepth(root)
    print("result:", res)