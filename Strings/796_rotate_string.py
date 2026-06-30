"""
LeetCode 796 - Rotate String
Approach:
- A rotated string must have the same length as the original string.
- We can iterate through the string `s`, and whenever we find a character that matches the first character of `goal`, we check if the rotation at this index matches `goal`.
- Note: A more optimal approach is `return len(s) == len(goal) and goal in s + s`, but the current approach simulates the rotations.
Time: O(N^2) worst case due to string slicing and comparison
Space: O(N) to store the rotated string during comparison
"""

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Rotated strings must be of the same length
        if len(s)!=len(goal):
            return False

        # If they are already identical, 0 rotations are needed
        if s==goal:
            return True

        # Try rotating at each index
        for i in range(len(s)):
            # Optimization: only check rotations starting with the first character of goal
            if s[i]==goal[0]:
                # Reconstruct the rotated string and compare
                if s[i:]+s[:i]==goal:
                    return True
        
        return False