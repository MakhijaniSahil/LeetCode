"""
LeetCode 653 - Two Sum IV - Input is a BST
Approach:
- Traverse the tree once while storing visited node values in a set.
- For each node, check whether its complement `k - node.val` has already been seen.
- If yes, a valid pair exists; otherwise continue the traversal.
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # A single node cannot form a pair.
        if not root.left and not root.right:
            return False

        # Track values seen so far during the traversal.
        seen = set()
        stack = [root]

        # Depth-first traversal over the tree.
        while stack:
            node = stack.pop()
            rem = k - node.val

            # If complement already exists, the target sum is found.
            if rem in seen:
                return True

            seen.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False
