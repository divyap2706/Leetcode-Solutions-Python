class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.findHeight(root.left)-self.findHeight(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def findHeight(self,root):
        if not root:
            return -1
        return 1+max(self.findHeight(root.left), self.findHeight(root.right))
    
