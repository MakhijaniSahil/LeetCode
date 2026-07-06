# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
LeetCode 450 - Delete Node in a BST
Approach:
- Recursively locate the node with value `key` using BST ordering.
- If node has 0 or 1 child, replace it with its child (or None).
- If node has 2 children, find its inorder successor (smallest in right subtree),
  copy the successor's value into current node, and delete the successor recursively.
Time: O(h) where h is tree height
Space: O(h) recursion stack
"""


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # Base case: empty subtree.
        if not root:
            return None

        # Recurse into left subtree when key is smaller.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Recurse into right subtree when key is larger.
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Found the node to delete.
            # Case 1 & 2: node has at most one child.
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: node has two children.
            # Find inorder successor (leftmost node in right subtree).
            succ = root.right
            while succ.left:
                succ = succ.left

            # Replace current node's value with successor's value.
            root.val = succ.val

            # Delete the successor node from right subtree.
            root.right = self.deleteNode(root.right, succ.val)

        return root