# LeetCode 124 - Binary Tree Maximum Path Sum
# Approach: DFS Recursion (track best global path)
# Time: O(n)
# Space: O(h)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Empty tree case.
        if not root:
            return 0

        # Store the best path sum seen anywhere in the tree.
        self.maxSum = float("-inf")

        def sum(root):
            # Null node contributes 0.
            if not root:
                return 0

            # Compute best downward sums from left and right children.
            sum_left = sum(root.left)
            sum_right = sum(root.right)

            # Path passing through current node (can include both sides if positive).
            curr_sum = root.val + max(0, sum_left, sum_right, sum_left + sum_right)

            # Update global maximum path sum.
            self.maxSum = max(self.maxSum, curr_sum)

            # Return best single-branch path to parent.
            return root.val + max(sum_left, sum_right, 0)

        # Run DFS from root and return the best path found.
        sum(root)
        return self.maxSum
