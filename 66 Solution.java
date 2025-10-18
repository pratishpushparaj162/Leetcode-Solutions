class Solution {
    public int[] plusOne(int[] digits) {
     int n=digits.length;
	        int i=n-1;
            if(n==1 && digits[0]<9){
                digits[0]=digits[0]+1;
                return digits;
            }
            if(n==1 && digits[0]==9){
                int[] res = new int[2];
                res[0]=1;
                res[1]=0;
                return res;
            }

	        System.out.println("Before while"+i);
	        while(digits[i]==9){
	            i--;
	            if(i<=0) { break;}
	        }
	        System.out.println(i);
	        int[] res = new int[n+1];
	        if(i==0 && digits[0]==9){
	            res[0]=1;
                    for(int j=1;j<n+1;j++){
                        res[j]=0;
                        }
	        }else{
	            digits[i]=digits[i]+1;
                for(int l=i+1;l<n;l++){
                    digits[l]=0;
                }
	            return digits;
	        }
	        
	        return res;
    }
}
