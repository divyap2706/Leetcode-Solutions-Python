class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal=[]
        self.helper(root,traversal)
        return traversal

    def helper(self,root,traversal):
        if root:
            self.helper(root.left, traversal)
            traversal.append(root.val)
            self.helper(root.right,traversal)

#Time complexity = O(n)
#Space complexity worst case=O(n)
#Average case space complexity=O(logn)
