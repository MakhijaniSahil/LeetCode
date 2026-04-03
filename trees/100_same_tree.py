# LeetCode 100 - Same Tree
# Approach: DFS Recursion (compare structure + values)
# Time: O(n)
# Space: O(h)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # If one node exists and the other doesn't, trees differ.
        if (not p and q) or (p and not q):
            return False
        # If both nodes are None, subtrees match.
        elif not p and not q:
            return True
        # If current values match, recursively compare left and right subtrees.
        elif p.val == q.val:
            return True and (
                self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            )
        # Value mismatch means trees are different.
        elif p.val != q.val:
            return False
