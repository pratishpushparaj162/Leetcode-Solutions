class Solution {
    public String convertToBase7(int num) {
        if(num==0)
        return "0";
        StringBuilder res=new StringBuilder();
        int ori=num;
        if(num<0){
            num=(-1)*(num);
        }
        while(num!=0){
            int rem=num%7;
            res.append(rem);
            num/=7;
        }
        if(ori<0){
            res.append("-");
        }
        return res.reverse().toString();
    }
}
