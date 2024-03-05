package org.example;

import java.util.List;

public class Main {
    public static void main(String[] args) {
//        int[] arr = {100, 50, 150, 10, 30, 200, 300};
        int[] arr = {100, 20, 200, 10, 30, 150, 300};
        BST bst = new BST();
        for (int i = 0; i < arr.length; i++) {
            bst.insert(arr[i]);
        }
        List<Integer> list = bst.bfs_traversal();
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i));
            if (i < list.size()-1) System.out.print("->");
        }
//        BST.Node node200 = bst.search(200);
//        System.out.println(node200.val);
//        System.out.println(node200.left);
//        System.out.println(node200.right.val);
//        List<Integer> li = bst.inorder_traversal();
//        for (int i = 0; i < li.size(); i++) {
//            System.out.print(li.get(i));
//            if (i < li.size()-1) System.out.print("->");
//        }
//        System.out.println();
//        bst.delete(100);
//        bst.delete(300);
//        bst.delete(50);
//        bst.delete(10);
//        bst.delete(30);
//        bst.delete(150);
//        bst.delete(200);
//        List<Integer> li2 = bst.inorder_traversal();
//        for (int i = 0; i < li2.size(); i++) {
//            System.out.print(li2.get(i));
//            if (i < li2.size()-1) System.out.print("->");
//        }
//        System.out.println();
    }
}