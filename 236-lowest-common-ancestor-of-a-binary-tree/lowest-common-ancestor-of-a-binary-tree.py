# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(node, p ,q):
            if node is None:
                return 
            l = LCA(node.left, p, q)
            r = LCA(node.right, p, q)

            if node == p or node == q:
                return node
            if l and r:
                return node
            return l or r
        
        return LCA(root, p, q)
        