class Solution:
    max_height = 0
    def get_height(self, node):
        if node is None:
            return 0

        left = self.get_height(node.left)
        right = self.get_height(node.right)
        return max(left, right) + 1

    def max_depth(self, root):
        return self.get_height(root)
