"""
LeetCode 1838 - Frequency of the Most Frequent Element
Approach:
- Sort the array first so that we only increment smaller numbers to match a larger target number.
- Use a sliding window approach. The right pointer expands the window by adding the current number to a running sum.
- The condition to check is if `(current_target * window_size) - current_sum > k`. If it is, the window is invalid because it requires more than `k` increments.
- When invalid, shrink the window from the left until it becomes valid again.
Time: O(n log n) due to sorting
Space: O(1)
"""

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort to easily increase smaller values to the current maximum in the window.
        nums.sort()
        left = 0
        max_freq = 1

        curr_sum = 0
        # Expand the window by moving the right pointer.
        for right in range(len(nums)):
            curr_sum += nums[right]
            # If the operations needed exceed k, shrink the window from the left.
            while (nums[right]*(right-left+1))-curr_sum>k:
                curr_sum -= nums[left]
                left+=1
            # Update the maximum frequency found so far.
            max_freq = max(max_freq, right-left+1)
        return max_freq