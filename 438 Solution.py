# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        if not root:
            return res

        path = []

        def dfs(n):
            nonlocal path, res, targetSum
            if not n:
                return

            path.append(n.val)
            
            if n.left:
                dfs(n.left)
                path.pop()
            
            if n.right:
                dfs(n.right)
                path.pop()
            

            sn = len(path)
            suffixes = [path.copy()[i:] for i in range(sn)]
            for suf in suffixes:
                if sum(suf) == targetSum:
                    res += 1

        
        dfs(root)
        
        return res

        
