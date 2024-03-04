class DoublyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None
    def __init__(self):
        self.head = None

    def prepend(self, val):
        node = self.Node(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        return node
    
    def append(self, val):
        walk = self.head
        while walk and walk.next:
            walk = walk.next
        node = self.Node(val)
        if not walk:
            self.head = node
        else:
            walk.next = node
            node.prev = walk
        return node
    
    def length(self):
        walk = self.head
        counter = 0
        while walk:
            counter += 1
            walk = walk.next
        return counter

    def node_at(self, idx):
        if idx < 0:
            return None
        counter = 0
        walk = self.head
        while walk:
            if counter == idx:
                return walk
            counter += 1
            walk = walk.next
        return None

    def insert(self, idx, val):
        if idx <= 0:
            return self.prepend(val)
        found = self.node_at(idx)
        if not found:
            return self.append(val)
        node = self.Node(val)
        found.prev.next = node
        node.prev = found.prev
        node.next = found
        found.prev = node
        return node

    def delete(self, val):
        walk = self.head
        while walk:
            if walk.val == val:
                break
            walk = walk.next
        if not walk:
            return None
        walk.prev.next = walk.next
        walk.next.prev = walk.prev
        return walk
    
    def back_and_forth(self):
        # traversal the doubly linked list forward to the end and then from the end backward to the beginning
        # returns a list
        arr = []
        walk = self.head
        walkback = None
        while walk:
            arr.append(walk.val)
            walkback = walk
            walk = walk.next
        while walkback:
            arr.append(walkback.val)
            walkback = walkback.prev
        return arr

    def to_list(self):
        walk = self.head
        li = []
        while walk:
            li.append(walk.val)
            walk = walk.next
        return li
    

if __name__ == "__main__":
    dll = DoublyLinkedList()
    for i in range(10):
        dll.append(i)
    print(dll.back_and_forth())
    # print(dll.to_list())
    # dll.insert(0, 200)
    # dll.insert(-1, 100)
    # dll.insert(3, 300)
    # dll.insert(1000, 400)
    # print(dll.to_list())
    # dll.delete(300)
    # print(dll.to_list())
    # dll.delete(1000)
    # print(dll.to_list())
    # print("length:", dll.length())
    # print(dll.node_at(9).val)
