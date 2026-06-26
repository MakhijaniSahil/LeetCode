"""
LeetCode 283 - Move Zeroes
Approach:
- Use a two-pointer approach (left and right).
- The `left` pointer tracks the position where the next non-zero element should go.
- The `right` pointer iterates through the array.
- If `nums[right]` is non-zero, it is swapped with `nums[left]`, effectively pushing zeroes to the right.
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 'l' points to the next available position for a non-zero element.
        l = 0
        
        # 'r' iterates through all elements in the array.
        for r in range(len(nums)):
            # If the element at 'l' is already non-zero, just advance 'l'.
            if nums[l]!=0:
                l+=1
                continue
            
            # If the current element at 'r' is zero, keep moving 'r' forward.
            if nums[r]==0:
                continue
                
            # Swap the non-zero element at 'r' with the zero at 'l'.
            nums[l],nums[r]=nums[r],nums[l]
            l+=1