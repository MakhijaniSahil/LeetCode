"""
LeetCode 704 - Binary Search
Approach:
- Use a recursive helper function to perform the binary search.
- Calculate the middle index. If the target is found at the middle, return the index.
- If the middle element is less than the target, recursively search the right half.
- If the middle element is greater than the target, recursively search the left half.
Time: O(log n)
Space: O(log n) due to recursion stack
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(l,h):
            # Base case: if the search space is invalid, target is not found.
            if l>h:
                return -1
            
            # Calculate the middle index.
            mid = (l+h)//2
            
            if nums[mid]==target:
                # Target found at the middle.
                return mid
            elif nums[mid]<target:
                # Target must be in the right half.
                return helper(mid+1,h)
            else:
                # Target must be in the left half.
                return helper(l,mid-1)
        # Initialize the search space boundaries.
        l=0
        h=len(nums)-1
        
        # Start the recursive search.
        return helper(l,h)