package org.example;

public class Stack {
    private int[] frames;
    private int top;
    private int size;

    public Stack(int size) {
        frames = new int[size];
        this.size = size;
        top = -1;
    }

    public void push(int val) throws Exception {
        if (top >= size - 1) {
            throw new Exception("stack overflow");
        }
        frames[++top] = val;
    }

    public int pop() throws Exception {
        if (top < 0) throw new Exception("empty stack");
        return frames[top--];
    }

    public int peek() throws Exception {
        if (top < 0) throw new Exception("empty stack");
        return frames[top];
    }

    public void clear() {
        top = -1;
    }
}
