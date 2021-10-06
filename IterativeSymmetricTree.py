class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack=[[root.left,root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val==right.val:
                stack.insert(0,[left.left,right.right])

                stack.insert(0,[left.right,right.left])
            else:
                return False
            return True
