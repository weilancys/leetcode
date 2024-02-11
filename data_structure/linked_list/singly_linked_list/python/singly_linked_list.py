class SinglyLinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
        
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node

    def add(self, value):
        self.prepend(value)

    def append(self, value):
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
            return
        walk = self.head
        while walk.next is not None:
            walk = walk.next
        walk.next = new_node

    def length(self):
        leng = 0
        walk = self.head
        while walk is not None:
            walk = walk.next
            leng += 1
        return leng
    
    def is_empty(self):
        return self.head is None
    
    def index(self, idx):
        if self.is_empty() or idx < 0 or idx >= self.length():
            raise IndexError("out of bounds")
        walk = self.head
        i = 0
        while i < idx:
            walk = walk.next
            i += 1
        return walk
    
    def search(self, value):
        walk = self.head
        while walk is not None:
            if walk.value == value:
                return walk
            walk = walk.next
        return walk
    
    def remove(self, value):
        walk = self.head
        prev = walk
        while walk is not None:
            if walk.value == value:
                if walk == self.head:
                    self.head = walk.next
                else:
                    prev.next = walk.next
                return walk
            else:
                prev = walk
                walk = walk.next
        return None
    
    def insert_at(self, index, value):
        if index < 0 or index >= self.length():
            raise IndexError("out of bounds")
        if index == 0:
            self.prepend(value)
            return
        i = 0
        walk = self.head
        while i < index-1:
            walk = walk.next
            i += 1
        new_node = self.Node(value)
        new_node.next = walk.next
        walk.next = new_node

    def print_list(self):
        if self.head is None:
            print("empty list")
            return
        print("head->", end="")
        walk = self.head
        while walk is not None:
            print(walk.value, end="->")
            walk = walk.next
        print("tail")
