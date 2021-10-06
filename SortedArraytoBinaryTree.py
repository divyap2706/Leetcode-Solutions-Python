class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convertBST(left,right):
            if (left>right):
                return None
            mid=(left+right)//2
            node=TreeNode(nums[mid])
            node.left=convertBST(left,mid-1)
            node.right=convertBST(mid+1,right)
            return node
        return convertBST(0,len(nums)-1)
