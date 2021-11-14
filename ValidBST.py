class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return ((check(node.left, left, node.val)) and check(node.right, node.val, right)) #to check if the left and right subtree is valid 
        
        return check(root, float("-inf"), float("inf"))  # node values can be betweeen - inf and + inf

    #Time complexity : O(n)