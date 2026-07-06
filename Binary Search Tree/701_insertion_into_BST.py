# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
LeetCode 701 - Insert into a Binary Search Tree
Approach:
- Use BST property to find the correct leaf position for `val`.
- Recursively descend left or right depending on comparison.
- When a null spot is found, create and return a new TreeNode.
Time: O(h) where h is the tree height
Space: O(h) recursion stack (can be made iterative to use O(1) space)
"""


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # If tree is empty, new node becomes root.
        if not root:
            return TreeNode(val)

        # Recurse into left subtree when value is smaller.
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Otherwise recurse into right subtree.
            root.right = self.insertIntoBST(root.right, val)

        # Return the (possibly unchanged) root up the call stack.
        return root