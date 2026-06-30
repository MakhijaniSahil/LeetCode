"""
LeetCode 205 - Isomorphic Strings
Approach:
- Use a hash map to store the one-to-one character mapping from string `s` to string `t`.
- Iterate through both strings simultaneously.
- If a character from `s` is already in the map, ensure it maps to the same character in `t`.
- If a character from `s` is not in the map, ensure that the character from `t` hasn't already been mapped to another character (using `map.values()`).
- If both checks pass, add the mapping.
Time: O(N) where N is the length of the strings (map size is bounded by the character set size).
Space: O(1) as the number of unique characters is fixed (e.g., ASCII).
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Dictionary to store character mappings from s to t
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                # If s[i] is already mapped, it must map to the current t[i]
                if map[s[i]]!=t[i]:
                    return False
            # If s[i] is not mapped but t[i] is already a value for some other character
            elif t[i] in map.values():
                return False
            else:
                # Create the new mapping
                map[s[i]] = t[i]
        
        return True