# LeetCode 110 - Balanced Binary Tree
# Approach 1: Brute Force (recompute subtree heights)
# Time: O(n^2)
# Approach 2: Optimal (postorder DFS: height + balanced)
# Time: O(n)
# Space: O(h)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Empty subtree has depth 0.
        if not root:
            return 0

        # Compute depth of left and right subtrees.
        left = root.left
        right = root.right

        # Current node adds 1 to the deeper subtree.
        return 1 + max(self.maxDepth(left), self.maxDepth(right))

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Empty tree is balanced.
        if not root:
            return True

        # Compare heights of left and right subtrees.
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)
        d = abs(depth_l - depth_r)
        if d <= 1:
            # If current node is balanced, recursively validate children.
            l = self.isBalanced(root.left)
            r = self.isBalanced(root.right)
        else:
            # Height difference more than 1 means unbalanced.
            return False

        if l and r:
            return True
        else:
            return False


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root):
            # Return [height, is_balanced] for each subtree.
            if not root:
                return [0, True]

            # Postorder traversal: compute child results first.
            left = dfs(root.left)
            right = dfs(root.right)

            # Current subtree is balanced if children are balanced and heights differ by at most 1.
            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            # Height is 1 + max(left_height, right_height).
            return [1 + max(left[0], right[0]), balanced]

        # Final answer is the balanced flag from the root.
        return dfs(root)[1]
