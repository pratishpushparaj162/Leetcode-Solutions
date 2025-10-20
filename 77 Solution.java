class Solution {
    List<List<Integer>> sol = new ArrayList<>();
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> ans = new ArrayList<>();
        backtrack(1, n, k, ans);
        return sol;
        
    }
    public void backtrack(int start, int n, int k, List<Integer> ans){
        if(ans.size() == k){
            sol.add(new ArrayList<>(ans));
            return;
        }
        for(int i = start; i <= n - (k - ans.size()) + 1; i++){
            ans.add(i);
            backtrack(i+1, n, k, ans);
            ans.remove(ans.size()-1);
        }
    }
}
