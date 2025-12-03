# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        q = deque()
        q.append(root)
        while len(q) != 0:
            count += 1
            for _ in range(len(q)):
                e = q.popleft()
                if e.left is not None:
                    q.append(e.left)
                if e.right is not None:
                    q.append(e.right)

        return count
        