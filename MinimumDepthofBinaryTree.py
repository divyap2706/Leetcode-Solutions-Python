class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left==None or root.right==None: #if its an unbalanced tree
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
