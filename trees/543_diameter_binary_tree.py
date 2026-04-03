# LeetCode 543 - Diameter of Binary Tree
# Approach 1: Brute Force (recompute heights for every node)
# Time: O(n^2)
# Approach 2: Optimal (single DFS traversal)
# Time: O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):  # Time Limit Exceeded (Didn't work)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Empty tree has diameter 0.
        if not root:
            return 0

        maxDiameter = 0

        def height(root):
            # Height of empty subtree is 0.
            if not root:
                return 0

            # Height = 1 + max(left_height, right_height).
            return 1 + max(height(root.left), height(root.right))

        # Try all possibilities: diameter through root, left subtree, right subtree.
        maxDiameter = max(
            maxDiameter,
            height(root.left) + height(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )
        return maxDiameter


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Track best diameter seen while computing heights.
        self.maxDiameter = 0

        def height(root):
            # Height of empty subtree is 0.
            if not root:
                return 0

            # Postorder: compute children first.
            left = height(root.left)
            right = height(root.right)

            # Diameter through current node is left_height + right_height.
            self.maxDiameter = max(self.maxDiameter, left + right)

            # Return subtree height to parent.
            return 1 + max(left, right)

        # Fill self.maxDiameter during DFS.
        height(root)
        return self.maxDiameter
