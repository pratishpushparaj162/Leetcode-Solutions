
class Solution {
    List<List<Integer>>temp=new ArrayList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root!=null) temp.add(new ArrayList<>(List.of(root.val)));
        else return temp;
        List<TreeNode>arr=new ArrayList<>();
        arr.add(root.left);
        arr.add(root.right);
        check(arr);
        return temp;
    }
    void check(List<TreeNode> head){
        List<Integer> level=new ArrayList<>();
        List<TreeNode> nextLevel=new ArrayList<>();
        for(TreeNode entry:head){
            if(entry!=null){
                level.add(entry.val);
                nextLevel.add(entry.left);
                nextLevel.add(entry.right);
            }
        }
        if(!level.isEmpty()){
            temp.add(level);
            check(nextLevel);
        }
    }
}
