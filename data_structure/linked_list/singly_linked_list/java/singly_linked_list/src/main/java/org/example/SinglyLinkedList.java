package org.example;

public class SinglyLinkedList {
    class Node {
        public int val;
        public Node next;
        public Node(int val) {
            this.val = val;
            next = null;
        }
    }

    private Node head;

    public SinglyLinkedList() {
        head = null;
    }

    Node prepend(int val) {
        Node node = new Node(val);
        node.next = head;
        head = node;
        return node;
    }

    Node append(int val) {
        Node walk = head;
        if (walk == null) {
            return prepend(val);
        }
        while (walk.next != null) {
            walk = walk.next;
        }
        walk.next = new Node(val);
        return walk.next;
    }

    void printList() {
        Node walk = head;
        while (walk != null) {
            System.out.print(walk.val);
            if (walk.next != null) System.out.print("->");
            walk = walk.next;
        }
        System.out.println();
    }

    Node nodeAt(int idx) {
        if (idx < 0) return null;
        int counter = 0;
        Node walk = head;
        while (walk != null) {
            if (counter == idx) return walk;
            counter++;
            walk = walk.next;
        }
        return null;
    }

    Node insert(int idx, int val) {
        if (idx <= 0) {
            return prepend(val);
        }
        Node walk = head;
        Node parent = null;
        int counter = 0;
        while (walk != null) {
            if (counter == idx) break;
            counter++;
            parent = walk;
            walk = walk.next;
        }
        if (parent == null) {
            return prepend(val);
        } else {
            Node node = new Node(val);
            parent.next = node;
            node.next = walk;
            return node;
        }
    }

    Node delete(int val) {
        Node walk = head;
        Node parent = null;
        while (walk != null) {
            if (walk.val == val) {
                if (parent == null) {
                    head = walk.next;
                } else {
                    parent.next = walk.next;
                }
                return walk;
            }
            parent = walk;
            walk = walk.next;
        }
        return null;
    }
}
