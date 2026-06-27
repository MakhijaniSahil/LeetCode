"""
LeetCode 35 - Search Insert Position
Approach:
- Use a recursive binary search to find the target.
- If the target is found, return its index.
- If the target is not found, the left pointer `l` will indicate the correct index to insert the target in sorted order.
Time: O(log n)
Space: O(log n) due to recursion stack
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(l,h):
            # Base case: search space is exhausted.
            # Return 'l' as it represents the correct insertion index.
            if l>h:
                return l
            
            # Calculate the middle index.
            mid=(l+h)//2
            
            if nums[mid]==target:
                # Target found at the middle index.
                return mid
            elif nums[mid]<target:
                # Target must be inserted or found in the right half.
                return helper(mid+1,h)
            else:
                # Target must be inserted or found in the left half.
                return helper(l,mid-1)
        # Initialize search space to the entire array.
        l=0
        h=len(nums)-1
        
        # Start the recursive search.
        return helper(l,h)