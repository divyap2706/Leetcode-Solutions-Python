class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root. right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

#Time complexity : O(n)
#Space complexity : Because of recursion, O(h) recursive calls will be added to the stack and since O(h) belongs to O(n) hence O(n) is the time complexity