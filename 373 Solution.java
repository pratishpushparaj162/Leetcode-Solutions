class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<List<Integer>> pq=new PriorityQueue<>((a,b)->(nums1[a.get(0)]+nums2[a.get(1)])-(nums1[b.get(0)]+nums2[b.get(1)]));
        for(int i=0;i<nums1.length;i++){
            pq.add(List.of(i,0));
        }
        int x,y;
        List<List<Integer>> res=new ArrayList<>();
        while(!pq.isEmpty() && k-->0){
            x=pq.peek().get(0);
            y=pq.peek().get(1);
            pq.poll();
            res.add(List.of(nums1[x],nums2[y]));
            if(++y<nums2.length){
                pq.add(List.of(x,y));
            }
        }
        return res;
    }
}
