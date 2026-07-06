from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
LeetCode 230 - Kth Smallest Element in a BST
Approach:
- Inorder traversal of BST yields sorted values in ascending order.
- Do iterative inorder (stack) to collect values until k-th is reached.
Time: O(h + k) where h is tree height (stack operations); worst-case O(n)
Space: O(h + k) for stack and collected values (can be optimized to O(h))
"""


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if not root:
            return None

        # Use deque as stack for iterative inorder.
        stack = deque()
        inorder = []

        # Standard iterative inorder: go left as far as possible, then visit, then go right.
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            inorder.append(root.val)

            # Early exit optimization: if we've collected k values, return k-th smallest.
            if len(inorder) == k:
                return inorder[-1]

            root = root.right

        # If k is within bounds, return the (k-1)th element.
        return inorder[k - 1] if 0 < k <= len(inorder) else None
