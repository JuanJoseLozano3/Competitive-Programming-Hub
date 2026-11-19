# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:      
        if(root == None):
            return TreeNode(val)
        
        r = root
        while True:
            if(r.val > val):
                if(r.left == None):
                    r.left = TreeNode(val)
                    break
                r = r.left
            else:
                if(r.right == None):
                    r.right = TreeNode(val)
                    break
                r = r.right

        return root