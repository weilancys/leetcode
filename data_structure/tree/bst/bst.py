# reference: https://www.javatpoint.com/binary-search-tree

class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.walk = None

    def add(self, val):
        if not self.root:
            new_node = self.Node(val)
            self.root = new_node
        else:
            if val < self.walk.val:
                if self.walk.left:
                    self.walk = self.walk.left
                    self.add(val)
                else:
                    new_node = self.Node(val)
                    self.walk.left = new_node
            elif val > self.walk.val:
                if self.walk.right:
                    self.walk = self.walk.right
                    self.add(val)
                else:
                    new_node = self.Node(val)
                    self.walk.right = new_node
            else:
                raise ValueError("bst should not contain identical values.")
        self.walk = self.root


if __name__ == "__main__":
    l = [45, 15, 79, 90, 10, 55, 12, 20, 50]
    bst = BST()
    for i in l:
        root = bst.add(i)
    print(bst.root.right.left.val) # should output 55
