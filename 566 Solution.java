class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
          if(mat.length* mat[0].length !=r*c) return mat;

        int[] array=new int[r*c];
        int k=0;
        for(int i=0;i<mat.length;i++){
            for(int j=0;j<mat[i].length;j++){
                array[k++]=mat[i][j];
            }
        }
        k=0;
        int[][] result=new int[r][c];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                result[i][j]=array[k++];
            }
        }
        return result;
        
    }
}
