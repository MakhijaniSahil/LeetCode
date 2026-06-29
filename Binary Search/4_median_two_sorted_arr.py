"""
LeetCode 4 - Median of Two Sorted Arrays
Approach:
- We can find the median by partitioning both arrays into two halves: a left half and a right half.
- To do this efficiently, we perform binary search on the smaller array (`nums1`).
- Let `i` be the partition in `nums1`, then the partition in `nums2` (`j`) is determined by the requirement that the left half must contain half of the total elements.
- The correct partition is found when the largest element in the left half of both arrays is smaller than or equal to the smallest element in the right half of both arrays (`nums1L <= nums2R` and `nums2L <= nums1R`).
- Edge cases where the partition is at the extremes are handled using +/- infinity.
Time: O(log(min(m, n))) where m and n are the lengths of the arrays.
Space: O(1)
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total//2

        # Ensure we always binary search on the smaller array to minimize time complexity
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1

        # Binary search boundaries for the smaller array
        l,r = 0 ,len(nums1)-1

        while True:
            i = (l+r)//2  # Partition index for nums1
            j = half - i - 2 # Partition index for nums2

            # Left and right boundary values for both arrays around the partitions.
            # Use -infinity/infinity for out of bounds to naturally satisfy inequalities.
            nums1L = nums1[i] if i>=0 else float('-inf')
            nums1R = nums1[i+1] if (i+1)<len(nums1) else float('inf')
            nums2L = nums2[j] if j>=0 else float('-inf')
            nums2R = nums2[j+1] if (j+1)<len(nums2) else float('inf')

            # Correct partition found
            if nums1L <= nums2R and nums2L <= nums1R:
                # If total length is odd, the median is the minimum of the right halves
                if total%2:
                    return float(min(nums1R, nums2R))
                # If even, the median is the average of the max left and min right
                else:
                    return (max(nums1L,nums2L) + min(nums1R , nums2R))/2.0
                
            # Partition in nums1 is too far right, move left
            elif nums1L > nums2R:
                r = i-1
            # Partition in nums1 is too far left, move right
            else:
                l = i+1