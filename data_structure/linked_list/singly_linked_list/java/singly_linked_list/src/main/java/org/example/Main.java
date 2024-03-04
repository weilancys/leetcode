package org.example;

public class Main {
    public static void main(String[] args) {
        SinglyLinkedList sll = new SinglyLinkedList();
        for (int i = 0; i < 10; i++) {
            sll.append(i);
//            sll.prepend(i);
        }
        sll.printList();
        SinglyLinkedList.Node node = sll.search(9);
        System.out.println(node.val);
        node = sll.search(1000);
        System.out.println(node);
        //System.out.printf("6th value: %d\n", sll.nodeAt(9).val);
//        sll.insert(-1, 100);
//        sll.insert(0, 200);
//        sll.insert(3, 300);
//        sll.insert(1000, 400);
//        sll.delete(300);
//        sll.delete(200);
//        sll.delete(100);
//        sll.delete(4);
//        sll.delete(400);
//        sll.delete(1000);
//        sll.printList();
    }
}