# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = maxi = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left < 0:
                left = 0
            right = dfs(root.right)
            if right < 0:
                right = 0
            nonlocal maxi
            maxi = max(maxi, left+root.val+right)
            return root.val + max(left, right)
        dfs(root)
        return maxi