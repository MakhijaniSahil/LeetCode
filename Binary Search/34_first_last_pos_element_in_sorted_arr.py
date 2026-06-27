"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array
Approach:
- Use two separate binary searches to find the leftmost and rightmost boundaries of the target.
- First Binary Search: Find the first occurrence by continuing to search the left half even after finding the target.
- Second Binary Search: Find the last occurrence by continuing to search the right half even after finding the target.
Time: O(log n)
Space: O(1)
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize result array with extreme values to represent 'not found'
        res = [float('inf') , float('-inf')]

        # First binary search: find the leftmost position
        l,h = 0 , len(nums)-1
        while l<=h:
            mid = (l+h)//2

            if nums[mid] == target:
                # Target found, record the minimum index and keep searching left
                res[0] = min(res[0] , mid)
                h = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                h = mid-1
        
        # Second binary search: find the rightmost position
        l,h = 0 , len(nums)-1
        while l<=h:
            mid = (l+h)//2

            if nums[mid] == target:
                # Target found, record the maximum index and keep searching right
                res[1] = max(res[1] , mid)
                l = mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                h = mid-1
        
        # If the first position is still infinity, target is not in the array
        return res if res[0]!= float('inf') else [-1,-1]

nums = [5,7,7,8,8,10]
target = 6
print(Solution().searchRange(nums,target))