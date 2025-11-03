
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {

        int ans = 0;

        Queue<Object[]> queue = new LinkedList<>();

        queue.add(new Object[] { root, 0 });

        while (queue.size() > 0) {

            Object[] arr = queue.poll();

            TreeNode temp = (TreeNode) arr[0];

            Integer val=( Integer) arr[1];

            if (temp.left != null) {
                queue.add(new Object[] { temp.left, 1 });

            }

            if (temp.right != null) {
                queue.add(new Object[] { temp.right, 2 });
            }

            if (temp.right == null && temp.left == null && val==1) {
                ans += temp.val;
            }

        }

        return ans;

    }
}
