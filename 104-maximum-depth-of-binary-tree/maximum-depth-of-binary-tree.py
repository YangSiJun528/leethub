import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth = 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            cur_node, level = q.popleft()
            max_depth = level
            for child in [cur_node.left, cur_node.right]:
                if child is not None:
                    q.append((child, level+1))
        return max_depth



        