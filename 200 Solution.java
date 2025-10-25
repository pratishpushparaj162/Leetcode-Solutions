class Solution(object):
    def dfs(self, grid, i, j, row, col):
        # Boundary and visited checks
        if i < 0 or i >= row or j < 0 or j >= col:
            return
        if grid[i][j] != '1':
            return

        grid[i][j] = "0"

        # Explore all four neighbors
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for di, dj in directions:
            self.dfs(grid, i + di, j + dj, row, col)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        # dfs
        # get the visited status array to store
        # grid can also be used as visited storage
        cnt = 0
        for i in range(row):
            for j in range(col):
                if(grid[i][j]=='1'):
                    self.dfs(grid, i, j, row, col)
                    cnt += 1
        return cnt
