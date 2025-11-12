/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Queue<TreeNode> q= new LinkedList<>();
        if(root==null){
            return ans;
        }
        q.offer(root);
        int level=0;
        int maxi=0;
        while(!q.isEmpty()){
            level=q.size();
            maxi=Integer.MIN_VALUE;
            for(int i=0;i<level;i++){
                TreeNode n=q.poll();
                if(n.left!=null) q.offer(n.left);
                if(n.right!=null) q.offer(n.right);
                maxi=Math.max(maxi,n.val);
            }
            ans.add(maxi);
        }
        return ans;
    }
}
