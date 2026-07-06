# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 114 - Flatten Binary Tree to Linked List
Approach:
- Recursively flatten left and right subtrees, tracking the end node of each
- Attach flattened left subtree as new right child, connecting original right as its tail
- Clear left pointer; return end of the new right subtree
Time: O(n)
Space: O(h) recursion stack
"""


class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # Base case: empty tree or leaf node.
        if not root or (not root.left and not root.right):
            return root
        
        # Recursively flatten left subtree; get its rightmost (end) node.
        end_left_subtree = self.flatten(root.left)
        
        # If left subtree exists, rewire it: insert flattened left as right child,
        # attach original right as tail of the flattened left subtree.
        if end_left_subtree:
            root.right, end_left_subtree.right = root.left, root.right
            root.left = None
        # Recursively flatten and return the end of the right subtree.
        return self.flatten(root.right)