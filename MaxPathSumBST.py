class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]   #global var to store the max
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)            #calculate max of the left path
            
            rightMax = dfs(root.right)          #calculate max of the right path
           #to avoid nodes with negative values in left and right path  
            leftMax = max(leftMax, 0)   
            rightMax = max(rightMax,0)  
            res[0] = max(res[0], root.val + leftMax + rightMax)       #calculating the maximum sum without split
            
            return root.val + max(leftMax, rightMax)     #passing max sum to the parent node with split
        
        dfs(root)
        return res[0]         
    
    
#Time complexity : O(n)
#Space complexity : O(logn) for a balanced tree and O(n) for an completely unbalanced tree