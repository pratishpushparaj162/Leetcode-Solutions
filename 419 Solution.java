class Solution {
    private int[][] dir = {
        {0, 1},
        {0, -1},
        {1, 0},
        {-1, 0}
    };
    private int m;
    private int n;

    public int countBattleships(char[][] board) {
        m = board.length;
        n = board[0].length;
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'X') {
                    ans++;
                    dfs(i, j, board);
                }
            }
        }
        return ans;
    }

    private void dfs(int x, int y, char[][] board) {
        if (x < 0 || x >= m || y < 0 || y >= n) {
            return;
        }
        if (board[x][y] == '.') {
            return;
        }
        board[x][y] = '.';
        for (int i = 0; i < 4; i++) {
            dfs(x + dir[i][0], y + dir[i][1], board);
        }
    }
}
