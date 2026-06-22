"""
LeetCode 1248 - Count Number of Nice Subarrays
Approach:
- Extract indices of all odd numbers.
- For each consecutive k-pair of odds, count valid subarrays between them.
- Multiply the even counts on both sides to get the number of valid placements.
Time: O(n)
Space: O(n)
"""


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Indices of all odd numbers, padded with boundaries.
        indices = [-1] + [i for i, num in enumerate(nums) if num % 2] + [len(nums)]

        # Not enough odd numbers to form k-odd subarrays.
        if len(indices) - 2 < k:
            return 0

        res = 0

        # Iterate through all consecutive k-pairs of odd indices.
        for i in range(1, len(indices) - k):
            left = i
            right = i + k - 1

            # Count even numbers between the left odd and its predecessor.
            left_evens = indices[left] - indices[left - 1]
            # Count even numbers between the right odd and its successor.
            right_evens = indices[right + 1] - indices[right]

            # Product gives all valid subarrays with exactly k odds in this window.
            res += left_evens * right_evens

        return res