"""
LeetCode 189 - Rotate Array
Approach 1 (Naive): 
- Rotate the array by 1 position, repeat this k times.
- Time: O(n*k) -> Results in TLE.
- Space: O(1)

Approach 2 (Optimal Reversal):
- Take k modulo n to avoid redundant rotations.
- Reverse the entire array.
- Reverse the first k elements.
- Reverse the remaining n-k elements.
Time: O(n)
Space: O(1)
"""

class Solution(object): #Got TLE
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Store the first element to correctly shift it to the next position.
        prev = nums[0]

        # Perform the 1-step rotation k times.
        for _ in range(k):
            for i in range(len(nums)):
                if i == len(nums)-1:
                    # Place the last shifted element at the beginning.
                    nums[0] = prev
                    break
                # Shift elements to the right.
                nums[i+1] , prev = prev , nums[i+1]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Normalize k in case it's larger than the array length.
        k= k % len(nums)
        # Reverse the entire array to bring the last k elements to the front.
        nums.reverse()
        # Restore the correct order for the first k elements.
        nums[:k] = reversed(nums[:k])
        # Restore the correct order for the remaining elements.
        nums[k:] = reversed(nums[k:])