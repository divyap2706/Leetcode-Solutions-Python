class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
             return self.isMirror(root.left,root.right)

    def isMirror(self,left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val==right.val:
                return self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
            else:
                return False
            
