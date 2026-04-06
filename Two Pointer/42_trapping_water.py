# LeetCode 42 - Trapping Rain Water
# Approach 1: Prefix/Suffix max arrays
# Time: O(n)
# Approach 2: Two Pointers
# Time: O(n)
# Space: O(1) for two-pointer approach

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Number of bars.
        n = len(height)

        # max_l[i] = max height to the left of i (excluding i).
        max_l = [0] * n
        # max_r[i] = max height to the right of i (excluding i).
        max_r = [0] * n
        # min_lr[i] = limiting boundary height at index i.
        min_lr = [0] * n

        # Build left max array.
        curr_max_l = 0
        for i in range(n):
            max_l[i] = curr_max_l
            curr_max_l = max(curr_max_l, height[i])

        # Build right max array.
        curr_max_r = 0
        for i in range(n - 1, -1, -1):
            max_r[i] = curr_max_r
            curr_max_r = max(curr_max_r, height[i])

        # Water level at i is bounded by the smaller side.
        for i in range(n):
            min_lr[i] = min(max_l[i], max_r[i])

        # Sum trapped water at each index.
        water = 0
        for i in range(n):
            curr_h = min_lr[i] - height[i]
            if curr_h > 0:
                water += curr_h

        return water


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two pointers from both ends.
        n = len(height)
        i = 0
        j = n - 1

        # Running maximum walls from left and right.
        max_l = 0
        max_r = 0
        water = 0

        # Move the side with smaller boundary; it determines trapped water.
        while i <= j:
            if max_l <= max_r:
                curr_h = max_l - height[i]
                if curr_h > 0:
                    water += curr_h
                max_l = max(max_l, height[i])
                i += 1
            else:
                curr_h = max_r - height[j]
                if curr_h > 0:
                    water += curr_h
                max_r = max(max_r, height[j])
                j -= 1

        return water
