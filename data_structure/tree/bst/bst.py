# references:
# https://www.javatpoint.com/binary-search-tree
# https://www.geeksforgeeks.org/binary-search-tree-traversal-inorder-preorder-post-order/

class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None

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


if __name__ == "__main__":
    # l = [45, 15, 79, 90, 10, 55, 12, 20, 50]
    # l = [45, 45, 45, 15, 79, 90, 10, 55, 12, 20, 50]
    l = [100, 20, 200, 10, 30, 150, 300]
    bst = BST()
    for i in l:
        bst.insert(i)
    # arr = bst.inorder_traversal()
    # node = bst.search(45)
    # print(node.val)
    
    print(bst.inorder_traversal())
    print(bst.preorder_traversal())
    print(bst.postorder_traversal())
