class Solution {
    int total = 0;

    public int function(TreeNode node) {
        if (node == null){
            return 0;
        }

        int l = function(node.left);
        int r = function(node.right);

        total += Math.abs(l-r);

        return node.val + l + r;
    }

    public int findTilt(TreeNode root) {
        function(root);
        return total;
    }
}
