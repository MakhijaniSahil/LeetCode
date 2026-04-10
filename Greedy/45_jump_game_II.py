# LeetCode 45 - Jump Game II
# Approach 1: Dynamic Programming (min jumps to each index)
# Time: O(n^2)
# Approach 2: Greedy level expansion
# Time: O(n)
# Space: O(1) for greedy approach


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # jumps[i] = minimum jumps needed to reach index i.
        n = len(nums)
        jumps = [float("inf")] * n
        jumps[0] = 0

        # Relax reachable positions from each index.
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    jumps[i + j] = min(jumps[i + j], 1 + jumps[i])

        # Minimum jumps needed to reach last index.
        return jumps[n - 1]


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # jumps = number of range expansions used so far.
        jumps = 0
        # far = farthest index reachable in current expansion.
        far = 0
        # end = boundary of current jump range.
        end = 0
        n = len(nums)

        # Traverse indices and expand jump range greedily.
        for i in range(n):
            if end == n - 1:
                break

            far = max(far, i + nums[i])

            # When reaching current boundary, we must take one jump.
            if i == end:
                jumps += 1
                end = far

        return jumps
