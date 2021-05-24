class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_valid_node(self, node):
        left_node, right_node = node.left, node.right
        
        if left_node is None and right_node is None:
            return True, node.val, node.val
        
        if left_node:
            left_valid, left_min, left_max = self.is_valid_node(node.left)
        
        if right_node:
            right_valid, right_min, right_max = self.is_valid_node(node.right)

        if left_valid and right_valid and right_min > node.val and left_max < node.val:
            return True, left_min, right_max
        
        return False, 0, 0

    def is_valid_bst(self, root):
        if root is None:
            return True
        
        is_valid, _, _ = self.is_valid_node(root)
        return is_valid
