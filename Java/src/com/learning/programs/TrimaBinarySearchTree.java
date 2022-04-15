package com.learning.programs;

class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
    }
 }


public class TrimaBinarySearchTree {

    public TreeNode trimBST(TreeNode root, int low, int high) {

        // Use binary search property - root.left.val < root.val < root.right.val
        // if root is < left of range then we can avoid traversing in left of root
        // if root is > right of range the we don't require to traverse in right subtree of root


        if(root==null) return null;

        if(low<=root.val && root.val<=high){
            // we can include root safely
            root.left = this.trimBST(root.left,low,high);
            root.right = this.trimBST(root.right,low,high);

            return root;
        }

        else if(root.val<low){
            return this.trimBST(root.right,low,high);
        }


        return this.trimBST(root.left,low,high);


    }
}
