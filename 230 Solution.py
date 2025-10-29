# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]

        def check(node):
            if node is None:
                return 0
            arr.append(node.val)
            check(node.left)
            check(node.right)
        
        check(root)
        
        arr.sort()

        return arr[k-1]
