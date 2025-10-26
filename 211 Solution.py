class Node:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr  = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["$"] = None

    def search(self, word: str) -> bool:
        
        def dfs(idx, curr):
            if idx == len(word):
                return "$" in curr
            
            c = word[idx]
            if c == ".":
                for c, child in curr.items():
                    if c == "$":
                        continue
                    if dfs(idx+1, child):
                        return True
                return False
            else:
                if c not in curr:
                    return False
                else:
                    return dfs(idx+1, curr[c])
        

        return dfs(0, self.root)
            
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
