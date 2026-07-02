"""
LeetCode 1781 - Sum of Beauty of All Substrings
Approaches included:
- Brute force (TLE): compute frequency for every substring using Counter
- Optimized sliding accumulation per start index using a 26-length freq

Time (optimized): O(n * 26) -> O(n)
Space: O(26) -> O(1)
"""

from collections import Counter


class Solution(object):
    # Brute-force solution: computes beauty for every substring directly.
    # Kept for reference; will TLE on large inputs.
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """

        def beauty(sub):
            freq = Counter(sub)
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            return max_freq - min_freq

        res = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                res += beauty(s[i:j])
        return res


class Solution(object):
    # Optimized: for each starting index i, expand j and maintain a
    # frequency array for 26 lowercase letters. At each extension, the
    # beauty is max_freq - min_freq where min_freq ignores zeros.
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for i in range(len(s)):
            freq = [0] * 26
            max_freq = 0
            # Expand the end index j from i to end, updating frequencies
            # and computing the current beauty in O(26) per step.
            for j in range(i, len(s)):
                idx = ord(s[j]) - ord("a")
                freq[idx] += 1
                if freq[idx] > max_freq:
                    max_freq = freq[idx]

                # Find minimum frequency among characters that appear (>0).
                min_freq = min(f for f in freq if f > 0)
                res += max_freq - min_freq

        return res
