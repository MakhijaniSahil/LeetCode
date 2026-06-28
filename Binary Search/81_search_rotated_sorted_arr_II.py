"""
LeetCode 81 - Search in Rotated Sorted Array II
Approach:
- Use binary search. The array is rotated, so at least one half of the array will always be sorted.
- If `nums[l] == nums[m]`, we cannot determine which half is sorted because of duplicates. In this case, simply shrink the search space by incrementing `l`.
- If the left half is sorted (`nums[l] < nums[m]`), check if the target lies within this half. If so, search the left half; otherwise, search the right half.
- If the right half is sorted, check if the target lies within this half. If so, search the right half; otherwise, search the left half.
Time: O(log n) average, O(n) worst case (when there are many duplicates)
Space: O(1)
"""

class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False
        l=0
        r=len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            
            # Skip duplicates to determine the sorted half.
            if nums[l]==nums[m]:
                l+=1
            # Left half is sorted.
            elif nums[l]<nums[m]:
                # Target is in the sorted left half.
                if nums[l]<= target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            # Right half is sorted.
            else:
                # Target is in the sorted right half.
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return False