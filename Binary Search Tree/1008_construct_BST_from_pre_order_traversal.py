# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
Approach:
- Use the preorder list and bounds to reconstruct BST in O(n) time.
- Maintain a global position `self.pos` through preorder list.
- For each recursive call, provide an upper bound; if current value exceeds it, return None.
- Create node, then build left subtree with upper bound = node.val, then right subtree with previous upper bound.
Time: O(n)
Space: O(h) recursion stack
"""


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Position pointer shared across recursion to consume preorder values exactly once.
        self.pos = 0
        n = len(preorder)

        def build(upper_bound):
            # If we've consumed all values or current value exceeds the allowable upper bound,
            # this subtree is empty.
            if self.pos >= n or preorder[self.pos] > upper_bound:
                return None

            # Take current value as node, advance position, and recursively build children.
            val = preorder[self.pos]
            node = TreeNode(val)
            self.pos += 1

            # Left subtree must have values < val.
            node.left = build(val)

            # Right subtree can have values up to the parent's upper_bound.
            node.right = build(upper_bound)

            return node

        # Start with +infinity upper bound.
        return build(float("inf"))
