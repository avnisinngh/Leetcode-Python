# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxdepth = 0
        hm = {}
        def dfs(root,depth):
            if not root:
                return 
            hm[root] = depth
            nonlocal maxdepth
            maxdepth = max(maxdepth, depth)
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)
        
        def lca(root):
            if not root or hm[root]==maxdepth:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                return root
            return left if left else right
        dfs(root,0)
        return lca(root)