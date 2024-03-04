package org.example;

public class Main {
    public static void main(String[] args) {
        DoublyLinkedList dll = new DoublyLinkedList();
        for (int i = 0; i < 10; i++) {
//            dll.prepend(i);
            dll.append(i);
        }
        dll.printList();
        for (int i = 0; i < 9; i++) {
            dll.delete(i);
        }
        dll.printList();
//        System.out.println(dll.search(4).val);
//        System.out.println(dll.search(1000));
//        System.out.printf("length: %d\n", dll.length());
//        dll.insert(-1, 100);
//        dll.insert(0, 50);
//        dll.insert(3, 300);
//        dll.insert(12, 400);
//        dll.printList();

        //System.out.printf("node 0: %d\n", dll.nodeAt(0).val);
    }
}