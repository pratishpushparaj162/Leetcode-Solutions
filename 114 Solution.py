class Solution(object):
    def flatten(self, root):
        head = root
        while root:
            if root.left:
                pred = root.left
                while pred.right:
                    pred = pred.right
                pred.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
            else:
                root = root.right
        return head
        
