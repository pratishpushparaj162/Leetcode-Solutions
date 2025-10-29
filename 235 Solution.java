/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    TreeNode help(TreeNode root, TreeNode p, TreeNode q)
    {
        if(root==null || root==p || root==q)return root;
        TreeNode left = help(root.left,p,q);
        TreeNode right = help(root.right,p,q);
        if(left!=null && right!=null)return root;
        return left==null?right:left;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return help(root,p,q);
    }
}
