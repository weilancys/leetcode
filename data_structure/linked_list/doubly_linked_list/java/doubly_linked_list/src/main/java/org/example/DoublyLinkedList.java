package org.example;

public class DoublyLinkedList {
    class Node {
        public int val;
        public Node prev;
        public Node next;

        public Node(int val) {
            this.val = val;
            prev = null;
            next = null;
        }
    }
    private Node head;

    public DoublyLinkedList() {
        head = null;
    }

    public Node prepend(int val) {
        Node node = new Node(val);
        node.next = head;
        if (head != null) head.prev = node;
        head = node;
        return node;
    }

    public Node append(int val) {
        if (head == null) {
            return prepend(val);
        }
        Node walk = head;
        while (walk.next != null) {
            walk = walk.next;
        }
        Node node = new Node(val);
        walk.next = node;
        node.prev = walk;
        return node;
    }

    public Node nodeAt(int idx) {
        if (idx < 0) return null;
        int counter = 0;
        Node walk = head;
        while (walk != null) {
            if (counter == idx) {
                return walk;
            }
            counter++;
            walk = walk.next;
        }
        return null;
    }

    public Node insert(int idx, int val) {
        if (idx <= 0 || head == null) return prepend(val);
        Node node = nodeAt(idx);
        if (node == null) {
            return append(val);
        } else {
            Node newNode = new Node(val);
            newNode.prev = node.prev;
            node.prev.next = newNode;
            newNode.next = node;
            node.prev = newNode;
            return newNode;
        }
    }

    public Node search(int val) {
        Node walk = head;
        while (walk != null) {
            if (walk.val == val) return walk;
            walk = walk.next;
        }
        return null;
    }

    public Node delete(int val) {
        Node found = search(val);
        if (found != null) {
            if (found.prev == null && found.next == null) {
                head = null;
            }
            else if (found.prev == null) {
                found.next.prev = null;
                head = found.next;
            } else if (found.next == null) {
                found.prev.next = null;
            } else {
                found.prev.next = found.next;
                found.next.prev = found.prev;
            }
            return found;
        }
        return null;
    }

    public int length() {
        Node walk = head;
        int counter = 0;
        while (walk != null) {
            counter++;
            walk = walk.next;
        }
        return counter;
    }

    public void printList() {
        Node walk = head;
        while (walk != null) {
            System.out.print(walk.val);
            if (walk.next != null) System.out.print("->");
            walk = walk.next;
        }
        System.out.println();
    }
}
