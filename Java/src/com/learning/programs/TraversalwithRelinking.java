package com.learning.programs;

public class TraversalwithRelinking {

    TreeNode head;
    TreeNode tail;

    public TreeNode increasingBST(TreeNode root) {

        inorder(root);

        return(head);

    }

    public void inorder(TreeNode root) {

        if(root== null) return;

        inorder(root.left);

        TreeNode nn = new TreeNode(root.val);
        // Do processing
        if(head == null){

            head = nn;
            tail = nn;

        }else{
            tail.right = nn;
            tail = tail.right;
        }

        inorder(root.right);

    }
}
