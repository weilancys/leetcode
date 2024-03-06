package org.example;

public class Queue {
    class Node {
        public int val;
        public Node next;

        public Node(int val) {
            this.val = val;
            next = null;
        }
    }

    private Node front;
    private Node rear;

    public Queue() {
        front = null;
        rear = null;
    }

    public Node enqueue(int val) {
        Node node = new Node(val);
        if (front == rear) {
            rear = node;
            if (front == null) {
                front = rear;
            } else {
                front.next = rear;
            }
        } else {
            rear.next = node;
            rear = rear.next;
        }
        return node;
    }

    public Node dequeue() {
        // remove a node from the front and return it
        // when removing from an empty queue, return null without throwing any exception
        Node deleted = null;
        if (front == rear) {
            if (rear == null) {
                return null;
            } else {
                deleted = front;
                front = null;
                rear = null;
            }
        } else {
            deleted = front;
            front = front.next;
        }
        return deleted;
    }

    public boolean isEmpty() {
        return rear == null;
    }

    public Node peek() {
        return front;
    }

    public void display() {
        if (front == null && rear == null) {
            System.out.println("empty queue");
            return;
        }
        Node walk = front;
        while (walk != null) {
            System.out.print(walk.val);
            if (walk.next != null) System.out.print("<-");
            walk = walk.next;
        }
        System.out.println();
    }

    public int size() {
        Node walk = front;
        int counter = 0;
        while (walk != null) {
            counter++;
            walk = walk.next;
        }
        return counter;
    }
}
