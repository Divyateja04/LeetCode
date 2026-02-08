class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    def isBalanced(self, root):
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False