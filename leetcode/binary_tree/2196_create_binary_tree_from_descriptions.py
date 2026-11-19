class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        exits = set()
        co = {}
        nodos = []

        for p,h,l in descriptions:
            if(p not in co):
                co[p] = TreeNode(p)
            if(h not in co):
                co[h] = TreeNode(h)

            pa = co[p]
            hi = co[h]

            nodos.append(p)
            exits.add(h)

            if(l == 0):
                pa.right = hi
            else:
                pa.left = hi

        for i in nodos:
            if(i not in exits):
                return co[i]

        return None