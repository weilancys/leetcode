# references:
# https://www.youtube.com/watch?v=gcULXE7ViZw
# https://www.geeksforgeeks.org/binary-search-tree-traversal-inorder-preorder-post-order/

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
        
    def depth(self, root: Node, level:int=0):
        if not root:
            return level - 1
        return max(self.depth(root.left, level+1), self.depth(root.right, level+1))


if __name__ == "__main__":
    # l = [45, 15, 79, 90, 10, 55, 12, 20, 50]
    # l = [45, 45, 45, 15, 79, 90, 10, 55, 12, 20, 50]
    # l = [100, 20, 200, 10, 30, 150, 300]
    l = [100, 20, 200, 10, 30, 150, 300, 40, 25, 50, 600,900, 1000]
    bst = BST()
    for i in l:
        bst.insert(i)

    d = bst.depth(bst.get_root())
    print("depth:", d)
    

    # trek = bst.path(30)
    # print([item.val for item in trek])

    # arr = bst.traversal_bfs()
    # print([item.val for item in arr])
    # arr = bst.inorder_traversal()
    # node = bst.search(45)
    # print(node.val)
    # bst.delete(200)
    # bst.delete(100)
    # bst.delete(300)
    # bst.delete(150)
    # bst.delete(20)
    # bst.delete(10)
    # bst.delete(30)
    # print([node.val for node in bst.inorder_traversal()])
    
    # print(bst.inorder_traversal())
    # print(bst.preorder_traversal())
    # print(bst.postorder_traversal())
