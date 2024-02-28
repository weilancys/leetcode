# reference: https://www.javatpoint.com/binary-search-tree

class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None

    def add(self, val):
        def _add(walk, val):
            if val < walk.val:
                if walk.left:
                    _add(walk.left, val)
                else:
                    new_node = self.Node(val)
                    walk.left = new_node
            elif val > walk.val:
                if walk.right:
                    _add(walk.right, val)
                else:
                    new_node = self.Node(val)
                    walk.right = new_node
            else:
                raise ValueError("bst should not contain identical values.")
        
        if self.__root:
            _add(self.__root, val)
        else:
            new_node = self.Node(val)
            self.__root = new_node
            
    def search(self, val):
        def _search(walk, val):
            if not walk:
                return
            elif walk.val == val:
                return walk
            elif val < walk.val:
                return _search(walk.left, val)
            elif val > walk.val:
                return _search(walk.right, val)
        return _search(self.__root, val)
        
    def traversal(self):
        arr = []
        def _traversal(node, list):
            if not node:
                return
            _traversal(node.left, arr)
            list.append(node.val)
            _traversal(node.right, arr)
        _traversal(self.__root, arr)
        return arr


if __name__ == "__main__":
    l = [45, 15, 79, 90, 10, 55, 12, 20, 50]
    bst = BST()
    for i in l:
        root = bst.add(i)
    arr = bst.traversal()
    print(arr)
