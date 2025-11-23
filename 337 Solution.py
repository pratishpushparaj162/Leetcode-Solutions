
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # even odd approach does not work because the thiefs may skip a second

        def traverse(node, depth=0):
            if not node:
                return 0, 0
            l_rob, l_notrob = traverse(node.left)
            r_rob, r_not_rob = traverse(node.right)
            p_rob = node.val + l_notrob + r_not_rob
            p_not_rob = max(l_rob, l_notrob) + max(r_rob, r_not_rob)
            return p_rob, p_not_rob

        return max(traverse(root))
