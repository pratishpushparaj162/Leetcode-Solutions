# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        in_map = {}

        def inorder(head):
            if head:
                inorder(head.left)
                in_map[head.val] = in_map.get(head.val, 0) + 1
                inorder(head.right)
        
        inorder(root)
        heap = []

        for k, v in in_map.items():
            heapq.heappush(heap, (-1 * v, k))
        
        cur = heapq.heappop(heap)
        mode = cur[0]
        ret = [cur[1]]
        while len(heap) > 0:
            cur = heapq.heappop(heap)
            if cur[0] == mode:
                ret.append(cur[1])
            else:
                break
        
        return ret
