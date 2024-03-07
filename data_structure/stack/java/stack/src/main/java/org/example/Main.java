package org.example;

public class Main {
    public static void main(String[] args) {
        Stack stack = new Stack(2);
        int[] arr = {0,1,2,3,4,5,6,7,8,9};
        for (int i = 0; i < arr.length; i++) {
            try {
                stack.push(arr[i]);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
        int i = 11;
        while (i > 0) {
            try {
                stack.pop();
            } catch (Exception e) {
                System.out.println(e);
            }
            i--;
        }
    }
}