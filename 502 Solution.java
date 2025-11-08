import java.util.PriorityQueue;

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<int[]> enough = new PriorityQueue<>((a,b)->b[0]-a[0]);
        PriorityQueue<int[]> noEnough = new PriorityQueue<>((a,b)->a[1]==b[1] ? b[0]-a[0] : a[1]-b[1]);
        for (int i = 0; i < profits.length; i++) {
            noEnough.offer(new int[]{profits[i], capital[i]});
        }
        while (k-->0){
            while (!noEnough.isEmpty() && noEnough.peek()[1] <= w){
                enough.offer(noEnough.poll());
            }
            if(enough.isEmpty())return w;
            w += enough.poll()[0];
        }
        return w;
    }
}
