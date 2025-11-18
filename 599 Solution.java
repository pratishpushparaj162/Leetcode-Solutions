class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        int min = Integer.MAX_VALUE;
        HashMap<String, Integer> map = new HashMap<>();
        List<String> res = new ArrayList<>();

        for(int i=0; i<list1.length; i++){
            String st = list1[i];
            map.put(st, i);
        }
        
        for(int i=0; i<list2.length; i++){
            String st = list2[i];
            if(map.containsKey(st)){
                int sum = i + map.get(list2[i]);
                if(sum < min){
                    res.clear();
                    res.add(list2[i]);
                    min = sum;
                } else if(sum == min){
                    res.add(list2[i]);
                }
            }
        }
        return res.toArray(new String[res.size()]);

    }
}
