package org.example;

public class Main {
    public static void main(String[] args) {
        Queue queue = new Queue();
        int[] arr = {1,2,3,4,5,6,7};
        for (int i = 0; i < arr.length; i++) {
            queue.enqueue(i);
        }
        System.out.printf("queue size: %d\n", queue.size());
        queue.display();
        System.out.println(queue.isEmpty());
        for (int i = 0; i < 8; i++) {
            queue.dequeue();
        }
        System.out.printf("after deletion, queue size: %d\n", queue.size());
        queue.display();
        System.out.println(queue.isEmpty());
    }
}