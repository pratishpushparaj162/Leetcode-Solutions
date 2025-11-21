class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0001 1100 -> 1
        # 1110 -> 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        def count_neighbors(i, j):
            total=0
            for dir_x, dir_y in directions:
                i_x = i+dir_x
                j_x = j+dir_y
                if i_x <0 or j_x<0 or i_x>=len(board) or j_x>=(len(board[0])):
                    continue
                total += board[i_x][j_x]%2
            return total

        # Calculating if it should be 1 or not
        for i in range(len(board)):
            for j in range(len(board[0])):
                numneighbors = count_neighbors(i, j)
                if numneighbors==3 or board[i][j]+numneighbors==3:
                    board[i][j] += 2
        
        # Finalizing each result
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=board[i][j]//2
        
                


        
