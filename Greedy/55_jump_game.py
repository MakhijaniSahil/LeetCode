# LeetCode 55 - Jump Game
# Approach 1: Reachability marking (visited array)
# Time: O(n^2)
# Approach 2: Greedy farthest reach
# Time: O(n)
# Space: O(1) for greedy approach


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # visited[i] indicates whether index i is reachable from index 0.
        visited = [False] * len(nums)
        visited[0] = True

        for i in range(len(nums)):
            # Expand jumps only from reachable indices.
            if visited[i] == True:
                for j in range(1, nums[i] + 1):
                    if (j + i) < len(nums):
                        visited[j + i] = True
                        # Early exit once last index becomes reachable.
                        if visited[-1]:
                            return True

        return visited[-1]


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # max_idx stores the farthest index reachable so far.
        max_idx = 0

        for i in range(len(nums)):
            # If current index is beyond reachable range, answer is False.
            if i > max_idx:
                return False

            # Update farthest reachable position.
            max_idx = max(max_idx, i + nums[i])

        # If loop finishes, every visited index was reachable.
        return True
