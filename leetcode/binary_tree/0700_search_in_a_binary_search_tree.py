# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        
        def dfs(nodo):
            if(nodo == None):
                return None
            if(nodo.val == val):
                return nodo
            izq = dfs(nodo.left)
            der = dfs(nodo.right)
            if izq != None:
                return izq
            elif der != None:
                return der
            else:
                return None
        
        return dfs(root)

        