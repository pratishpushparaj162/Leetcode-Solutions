class Solution {
    final int N = 9;
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < N; i++) {
            if (isRowValid(board[i]) == false || isColumnValid(board, i) == false) return false;
            for (int j = 0; j < N; j++) {
                if (i % 3 == 0 && j % 3 == 0) {
                    if (isSquareValid(board, i, j) == false) return false;
                }
            }
        }
        
        return true;
    }
    public boolean isRowValid(char[] row) {
        var seen = new int[9];
        int num;
        for (int i = 0; i < N; i++) {
            if (row[i] == '.') continue;
            
            num = row[i] - '0';
            if (seen[num - 1] == 1) return false;
            else seen[num - 1] = 1;  
        }
        return true;
    }
    public boolean isColumnValid(char[][] board, int c) {
        int num;
        var seen = new int[N];
        for (int i = 0; i < N; i++) {
            if (board[i][c] == '.') continue;
            
            num = board[i][c] - '0';
            if (seen[num - 1] == 1) return false;
            else seen[num - 1] = 1;
            
        }
        return true;
    }

    public boolean isSquareValid(char[][] board, int row, int col) {
        var seen = new int[N];
        int num;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[row + i][col + j] == '.') continue;
                num = board[i + row][j + col] - '0';
                if (seen[num - 1] == 1) return false;
                seen[num - 1] = 1;
            }
        }
        return true;
    }
}
