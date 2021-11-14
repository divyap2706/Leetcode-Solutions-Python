class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)

#Time complexity : O(n)
#Space complexity: O(logn) for balanced tree and worst case O(logn) for totally unbalanced tree
#Recursive approach
