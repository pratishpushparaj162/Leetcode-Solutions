class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        Traverse(root,list);
        return list;
    }
    public void Traverse(TreeNode root, List<Integer> list){
        if(root == null){
            return;
        }
        Traverse(root.left,list);
        list.add(root.val);
        Traverse(root.right, list);
    }
}
