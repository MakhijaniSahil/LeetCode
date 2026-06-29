"""
LeetCode 1539 - Kth Missing Positive Number
Approach:
- Use binary search on the array indices.
- At any index `mid`, the number of missing positive integers before `arr[mid]` is `arr[mid] - mid - 1`.
- If this count is >= k, it means the kth missing number is to the left of `mid`.
- If the count is < k, the kth missing number is to the right of `mid`.
- After the loop, `l` points to the index where the kth missing number should be inserted, and the result can be calculated as `l + k`.
Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # Initialize binary search boundaries on the indices of the array.
        l = 0
        r = len(arr)-1

        while l<=r:
            mid = (l+r)//2

            # Number of missing integers before arr[mid] is arr[mid] - mid - 1
            # If the missing count is >= k, we look in the left half.
            if arr[mid]-mid-1>=k:
                r = mid-1
            # Otherwise, we need more missing numbers, so we look in the right half.
            else:
                l = mid+1
        
        # l is now the number of existing elements smaller than the kth missing number.
        # Thus, the kth missing number is exactly l + k.
        return l+k