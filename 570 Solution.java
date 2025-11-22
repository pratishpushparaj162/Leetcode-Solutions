
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        preorder(root, sb1);
        preorder(subRoot, sb2);
        return (sb1.toString().contains(sb2.toString())) ;
    }

    private void preorder(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("#");
            return;
        }
        sb.append(":" + node.val);
        preorder(node.left, sb);
        preorder(node.right, sb);
    }

}
