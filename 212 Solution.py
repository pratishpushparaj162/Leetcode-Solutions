class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d, m, n, self.result = {}, len(board), len(board[0]), set()

        for word in words:
            cur_d = d
            if not word: continue
            c = word
            while c:
                s, c = c[0], c[1:]
                if s not in cur_d: cur_d[s] = {}
                cur_d = cur_d[s]
            if "end" not in cur_d: cur_d["end"] = word

        offs = [[-1, 0],[1, 0],[0, -1],[0, 1]]
        def dfs(i, j, word_d):
            if board[i][j] == "*": return
            temp = board[i][j]
            board[i][j] = "*"

            if "end" in word_d:
                if word_d["end"] not in self.result: self.result.add(word_d["end"])
                
            for off in offs:
                i_off, j_off = i+off[0], j+off[1]
                if not(-1<i_off<m and -1<j_off<n): continue
                if board[i_off][j_off] in word_d:
                    dfs(i_off, j_off, word_d[board[i_off][j_off]])
            
            board[i][j] = temp
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in d:
                    dfs(i, j, d[board[i][j]])
        return list(self.result)
