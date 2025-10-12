class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1 || numRows > s.length()){
            return s;
        }

        int currList = 0;
        int increment = 1;

        StringBuilder arr[] = new StringBuilder[numRows];

        for(int i=0;i<arr.length;i++){
            arr[i] = new StringBuilder();
        }

        for(char ch : s.toCharArray()){
            arr[currList].append(ch);

            if(currList == 0){
                increment = 1;
            }else if(currList == numRows - 1){
                increment = -1;
            }

            currList += increment;
        }

        StringBuilder sb = new StringBuilder();

        for(int i=0;i<arr.length;i++){
            sb.append(arr[i]);
        }

        return sb.toString();
    }
}
