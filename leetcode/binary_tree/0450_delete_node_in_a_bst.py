class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            sucesor = root.right

            while sucesor.left:
                sucesor = sucesor.left

            root.val = sucesor.val
            root.right = self.deleteNode(root.right, sucesor.val)

        return root