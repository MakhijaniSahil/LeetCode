from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 173 - Binary Search Tree Iterator
Approach:
- Use a stack to perform inorder traversal on-demand (lazy approach).
- Init: push all left-most nodes onto stack.
- next(): pop a node (next in inorder), then push all left-most nodes of its right subtree.
- hasNext(): check if stack is non-empty.
Time: O(1) amortized per operation
Space: O(h) stack space
"""


class BSTIterator:
    """
    An iterator over a BST that yields values in sorted (inorder) order.
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize the iterator with the root of a BST.
        Preprocess: push all left-most nodes onto the stack.
        """
        self.stack = []
        # Go to the leftmost node.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        Return the next smallest value in the BST.
        """
        # Pop the node with the smallest unvisited value.
        res = self.stack.pop()

        # Process the right subtree: push all left-most nodes of right subtree.
        node = res.right
        while node:
            self.stack.append(node)
            node = node.left

        return res.val

    def hasNext(self) -> bool:
        """
        Return True if there are more elements to iterate.
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
