# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        mas = 0
        def dfs(nodo, valor):
            nonlocal mas 
            if nodo is None or nodo.val != valor:
                return 0
            izq = dfs(nodo.left,valor)
            der = dfs(nodo.right,valor)
            mas = max(mas, izq+der)
            return 1 + max(izq,der)

        mas = 0
        pila = [root]
        while pila:
            nodo = pila.pop()
            if nodo:
                if nodo.left:
                    pila.append(nodo.left)
                if nodo.right:
                    pila.append(nodo.right)
                
                dfs(nodo,nodo.val)

        return mas



        