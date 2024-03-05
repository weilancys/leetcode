package org.example;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class BST {
    class Node {
        public int val;
        public Node left;
        public Node right;

        public Node(int val) {
            this.val = val;
            left = null;
            right = null;
        }
    }

    private Node root;

    public BST() {
        root = null;
    }

    private Node _insert(Node current, int val) {
        if (current == null) return new Node(val);
        if (val < current.val) {
            current.left = _insert(current.left, val);
        } else if (val > current.val) {
            current.right = _insert(current.right, val);
        }
        return current;
    }

    public Node insert(int val) {
        root = _insert(root, val);
        return root;
    }

    public Node search(int val) {
        Node walk = root;
        while (walk != null) {
            if (walk.val == val) return walk;
            else if (val < walk.val) walk = walk.left;
            else walk = walk.right;
        }
        return null;
    }

    public Node findMin(Node current) {
        // find node with the minimal value in a subtree
        if (current == null) return null;
        while (current.left != null) current = current.left;
        return current;
    }

    public Node delete(int val) {
        if (root == null) return null;
        Node walk = root;
        Node parent = null;
        while (walk != null) {
            if (walk.val == val) break;
            parent = walk;
            if (val < walk.val) walk = walk.left;
            else walk = walk.right;
        }
        if (walk.left == null && walk.right == null) {
            if (parent == null) {
                root = null;
                return walk;
            }
            if (parent.left == walk) parent.left = null;
            else if (parent.right == walk) parent.right = null;
            return walk;
        } else if (walk.left != null && walk.right != null) {
            Node walk_inorder = walk.right;
            Node walk_inorder_parent = walk;
            while (walk_inorder.left != null) {
                walk_inorder_parent = walk_inorder;
                walk_inorder = walk_inorder.left;
            }
            int temp = walk.val;
            walk.val = walk_inorder.val;
            walk_inorder.val = temp;
            if (walk_inorder.right != null) {
                if (walk_inorder_parent.left == walk_inorder) {
                    walk_inorder_parent.left = walk_inorder.right;
                } else if (walk_inorder_parent.right == walk_inorder) {
                    walk_inorder_parent.right = walk_inorder.right;
                }
            }
            else walk_inorder_parent.left = null;
            return walk_inorder;
        } else {
            if (parent == null) {
                if (walk.left == null) root = walk.right;
                else if (walk.right == null) root = walk.left;
                return walk;
            }
            if (walk.left == null) {
                if (parent.left == walk) {
                    parent.left = walk.right;
                } else if (parent.right == walk) {
                    parent.right = walk.right;
                }
                return walk;
            } else if (walk.right == null) {
                if (parent.left == walk) {
                    parent.left = walk.left;
                } else if (parent.right == walk) {
                    parent.right = walk.left;
                }
                return walk;
            }
        }
        return walk;
    }

    public List<Integer> inorder_traversal() {
        List<Integer> arr = new ArrayList<>();
        _inorder(root, arr);
        return arr;
    }

    private void _inorder(Node current, List<Integer> arr) {
        if (current == null) return;
        _inorder(current.left, arr);
        arr.add(current.val);
        _inorder(current.right, arr);
    }

    public List<Integer> preorder_traversal() {
        List<Integer> arr = new ArrayList<>();
        _preorder(root, arr);
        return arr;
    }

    private void _preorder(Node current, List<Integer> arr) {
        if (current == null) return;
        arr.add(current.val);
        _preorder(current.left, arr);
        _preorder(current.right, arr);
    }

    public List<Integer> postorder_traversal() {
        List<Integer> arr = new ArrayList<>();
        _postorder(root, arr);
        return arr;
    }

    private void _postorder(Node current, List<Integer> arr) {
        if (current == null) return;
        _postorder(current.left, arr);
        _postorder(current.right, arr);
        arr.add(current.val);
    }

    public List<Integer> bfs_traversal() {
        // traversal in bfs manner
        if (root == null) return new LinkedList<>();
        Queue<Node> queue = new LinkedList<>();
        List<Integer> arr = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            arr.add(current.val);
            if (current.left != null) queue.add(current.left);
            if (current.right != null) queue.add(current.right);
        }
        return arr;
    }
}
