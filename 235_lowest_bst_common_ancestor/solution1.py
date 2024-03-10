# first find the path to p and q as two arrays
# then find the last common item in both the arrays
# the last common item is the LCA
# the below solution used a bst implementation of my own with a little tweaks

# space complexity: O(n)
# time complexity: O(n) ?

# Definition for a binary tree node.
# class BST.Node:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None
        self.path_found = False
    
    def get_root(self):
        return self.__root

    def __insert(self, walk, val):
        if walk is None:
            node = self.Node(val)
            return node
        elif val < walk.val:
            walk.left = self.__insert(walk.left, val)
            return walk
        elif val > walk.val:
            walk.right = self.__insert(walk.right, val)
            return walk
        else:
            return walk

    def insert(self, val):
        self.__root = self.__insert(self.__root, val)

    def __search_recursive(self, walk, val):
        # search for a node in bst in recursive manner
        if not walk:
            return
        elif walk.val == val:
            return walk
        elif val < walk.val:
            return self.__search(walk.left, val)
        elif val > walk.val:
            return self.__search(walk.right, val)
    
    def __search_loop(self, walk, val):
        # search for a node in bst in loop manner
        while walk:
            if walk.val == val:
                return walk
            elif val < walk.val:
                walk = walk.left
            elif val > walk.val:
                walk = walk.right
        return None
            
    def search(self, val):
        return self.__search_loop(self.__root, val)
        
    def inorder_traversal(self):
        arr = []
        def _traversal(node, list):
            if not node:
                return
            _traversal(node.left, arr)
            list.append(node)
            _traversal(node.right, arr)
        _traversal(self.__root, arr)
        return arr
    
    def preorder_traversal(self):
        arr = []
        def _traversal(node, list):
            if not node:
                return
            list.append(node)
            _traversal(node.left, arr)
            _traversal(node.right, arr)
        _traversal(self.__root, arr)
        return arr
 
    def postorder_traversal(self):
        arr = []
        def _traversal(node, list):
            if not node:
                return
            _traversal(node.left, arr)
            _traversal(node.right, arr)
            list.append(node)
        _traversal(self.__root, arr)
        return arr
    
    def traversal_bfs(self):
        # traversal in bfs manner
        if not self.__root:
            return []
        queue = []
        arr = []
        queue.append(self.__root)
        while queue:
            elem = queue.pop(0)
            arr.append(elem)
            if elem.left:
                queue.append(elem.left)
            if elem.right:
                queue.append(elem.right)
        return arr
    
    def __find_min(self, root):
        walk = root
        while walk and walk.left:
            walk = walk.left
        return walk

    def delete(self, val):
        walk = self.__root
        parent = None
        while walk:
            if walk.val == val:
                break
            elif val < walk.val:
                parent = walk
                walk = walk.left
            elif val > walk.val:
                parent = walk
                walk = walk.right
        if walk is None:
            return
        if walk.left is None and walk.right is None:
            if parent is None: # deleing the only one root node
                self.__root = None
                return
            if parent.left == walk:
                parent.left = None
            elif parent.right == walk:
                parent.right = None
            return walk
        elif walk.left and walk.right:
            walk_inorder = walk.right
            walk_inorder_parent = walk
            while walk_inorder.left:
                walk_inorder_parent = walk_inorder
                walk_inorder = walk_inorder.left
            temp = walk.val
            walk.val = walk_inorder.val
            walk_inorder.val = temp
            if walk_inorder_parent.left == walk_inorder:
                walk_inorder_parent.left = None
            elif walk_inorder_parent.right == walk_inorder:
                walk_inorder_parent.right = None
            return walk_inorder
        else:
            if walk == self.__root:
                if walk.left:
                    self.__root = walk.left
                elif walk.right:
                    self.__root = walk.right
            else:
                if parent.left == walk:
                    if walk.left:
                        parent.left = walk.left
                    elif walk.right:
                        parent.left = walk.right
                elif parent.right == walk:
                    if walk.left:
                        parent.right = walk.left
                    elif walk.right:
                        parent.right = walk.right
            return walk 
    
    def path(self, val) -> list:
        # search for path to the node with val
        # returns a list indicating the path
        self.path_found = False
        trek = []
        self.__path(self.__root, val, trek)
        return trek
    
    def __path(self, current: Node, val: int, trek: list):
        # used by path() method
        # introduced a self.path_found instance variable
        if not current or self.path_found:
            return
        if current not in trek:
            trek.append(current)
        if current.val == val:
            self.path_found = True
            return
        self.__path(current.left, val, trek)
        self.__path(current.right, val, trek)
        if not self.path_found:
            trek.remove(current)


class Solution:
    def __init__(self) -> None:
        self.found = False
        self.path_p = []
        self.path_q = []

    def lowestCommonAncestor(self, root: BST.Node, p: BST.Node, q: BST.Node) -> BST.Node:
        self.found =False
        self.find_path(root, p, self.path_p)
        self.found = False
        self.find_path(root, q, self.path_q)
        lca = None
        idx = 0
        while idx < min(len(self.path_p), len(self.path_q)) and self.path_p[idx] == self.path_q[idx]:
            lca = self.path_p[idx]
            idx += 1
        return lca
        
    def find_path(self, current: BST.Node, target: BST.Node, path: list):
        if not current or self.found:
            return
        if current not in path:
            path.append(current)
        if current == target:
            self.found = True
            return
        self.find_path(current.left, target, path)
        self.find_path(current.right, target, path)
        if not self.found:
            path.remove(current)


if __name__ == "__main__":
    solution1 = Solution()
    bst = BST()
    input_list = [6,2,8,0,4,7,9,3,5]
    for item in input_list:
        bst.insert(item)
    lca = solution1.lowestCommonAncestor(bst.get_root(), bst.search(2), bst.search(4))
    print("lca", lca.val)