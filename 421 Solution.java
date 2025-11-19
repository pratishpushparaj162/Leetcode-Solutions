class Solution {
    public int findMaximumXOR(int[] nums) {
        TrieNode root = new TrieNode();
        for(int i=0;i<nums.length;i++){
            insert(root,nums[i]);
        }
        int max=0;
        for(int i=0;i<nums.length;i++){
            max = Math.max(maxXor(root,nums[i]),max);
        }
        return max;
    }
    public void insert(TrieNode root,int num){
        TrieNode curr =root;
        for(int i=31;i>=0;i--){
            int mask = (num>>i) &1;
            if(curr.children[mask] ==null){
                curr.children[mask] = new TrieNode();
            }
            curr = curr.children[mask];
        }
    }
    public int maxXor(TrieNode root,int num){
        int xor=0;
        TrieNode curr = root;
        for(int i=31;i>=0;i--){
            int mask = (num>>i) & 1;
            int opp= 1-mask;
            if(curr.children[opp]!=null){
                xor = xor | (1<<i);
                curr = curr.children[opp];
            }else{
                curr = curr.children[mask];
            }
        }
        return xor;
    }
}
class TrieNode{
    TrieNode[] children = new TrieNode[2]; 
}
