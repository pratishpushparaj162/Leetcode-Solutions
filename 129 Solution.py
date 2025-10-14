# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        def dfs(node):
            if node.left is None and node.right is None:
                return [(node.val, 0)]
            cur_val = node.val
            res_l = []
            res_r = []
            if node.left:
                res_left = dfs(node.left)
                for num, index in res_left:
                    res_l.append((cur_val * (10 ** (index + 1)) + num, index + 1))
            if node.right:
                res_right = dfs(node.right)
                for num, index in res_right:
                    res_r.append((cur_val * (10 ** (index + 1)) + num, index + 1))
            return res_l + res_r
        res = dfs(root)
        return sum([num for num, _ in res])
