"""
LeetCode 2149 - Rearrange Array Elements by Sign
Approach 1 (Two Pass):
- Create two separate arrays for positive and negative numbers.
- Iterate through both arrays and alternately append elements to the result array.
- Time: O(n)
- Space: O(n)

Approach 2 (One Pass):
- Create a result array of the same length.
- Use two pointers: `pos` starting at index 0 and `neg` starting at index 1.
- Iterate through the array once. Place positive numbers at `pos` (incrementing by 2) and negative numbers at `neg` (incrementing by 2).
- Time: O(n)
- Space: O(n)
"""

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Separate the positive and negative numbers into two lists.
        pos = [n for n in nums if n>0]
        neg = [n for n in nums if n<0]
        
        # Interleave the positive and negative numbers.
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize pointers for the next available positive and negative indices.
        pos = 0
        neg = 1
        n = len(nums)

        # Pre-allocate the result array to avoid dynamic resizing.
        res = [0]*n

        # Iterate through the array and place elements directly into their correct positions.
        for i in range(n):
            if nums[i]>0:
                res[pos]=nums[i]
                pos+=2
            else:
                res[neg]=nums[i]
                neg+=2
        return res