class Solution {
    //find the flowing area for both pacific and Atlantic 
    //then return the intersection part
    int m;
    int n;
    int[][] directions = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        m = heights.length;
        n = heights[0].length; 
        List<List<Integer>> intersection = new ArrayList<>();

        //left and top boundary
        boolean[][] pacificArea = new boolean[m][n];
        //right and bottom boundary
        boolean[][] atlanticArea = new boolean[m][n];
        for(int i = 0; i < m; i++){
            dfs(i,0,heights,pacificArea);
            dfs(i,n-1,heights,atlanticArea);
        }
        for(int j = 0; j < n; j++){
            dfs(0,j,heights,pacificArea);
            dfs(m-1,j,heights,atlanticArea);
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(atlanticArea[i][j] && pacificArea[i][j]){
                    ArrayList<Integer> path = new ArrayList<>();
                    path.add(i);
                    path.add(j);
                    intersection.add(new ArrayList<>(path));
                }
            }
        }

        return intersection;
    }

    private void dfs(int i, int j, int[][] matrix, boolean[][] area){
        area[i][j]=true;
        for(int[] d : directions){
            int x = d[0]+i, y = d[1]+j;
            if(x < 0|| y <0 || x >=m || y >=n || area[x][y]){
                continue;
            }
            if(!area[x][y] && matrix[x][y] >= matrix[i][j]){
                dfs(x, y, matrix, area);
            }
        }
    }
}
