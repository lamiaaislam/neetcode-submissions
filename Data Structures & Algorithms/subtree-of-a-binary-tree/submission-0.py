# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. Base Case: An empty subRoot is always a subtree of any tree
        if not subRoot:
            return True
        
        # 2. Base Case: If main root is empty but subRoot isn't, it cannot be a subtree
        if not root:
            return False
        
        # 3. Check if trees rooted at 'root' and 'subRoot' are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # 4. Recursively check if subRoot is in the left OR right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 5. Base Case: Both nodes are empty (reached leaf boundaries simultaneously)
        if not p and not q:
            return True
        
        # 6. Base Case: One node is missing, or node values don't match
        if not p or not q or p.val != q.val:
            return False
        
        # 7. Recursively check if both left and right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)