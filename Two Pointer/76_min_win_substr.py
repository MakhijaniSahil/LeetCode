"""
LeetCode 76 - Minimum Window Substring
Approach 1: Sliding Window with Required Counts
- Build the required character counts from t.
- Expand the window and shrink while all required counts are satisfied.
Time: O(n * unique(t))
Space: O(unique(t))

Approach 2: Sliding Window with Have/Need
- Track how many required characters are fully matched in the current window.
- Shrink the left edge while all required characters are covered.
Time: O(n)
Space: O(unique(s) + unique(t))
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Lengths of source and target strings.
        m = len(s)
        n = len(t)

        # Source shorter than target can never contain a valid window.
        if m < n:
            return ""

        # Track the best window found so far.
        ans = ""
        curr_len = float("inf")
        i = 0

        # Required character counts from t.
        count = {}
        for c in t:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        # Expand the right edge of the window.
        for j in range(m):
            if s[j] in count:
                count[s[j]] -= 1

                # Shrink while the current window contains all required chars.
                while all(count[c] <= 0 for c in count) and i <= j:
                    if j - i + 1 < curr_len:
                        curr_len = j - i + 1
                        ans = s[i:j + 1]
                    if s[i] in count:
                        count[s[i]] += 1
                    i += 1

            # Skip over characters that are outside the target set.
            if i == j and s[j] not in count:
                i += 1
        return ans


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Empty target or impossible length means no valid window.
        if t == "":
            return ""

        if len(s) < len(t):
            return ""

        # Required counts and current window counts.
        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have counts fully matched characters, need is total required types.
        have = 0
        need = len(countT)
        res = ""
        res_len = float("inf")
        l = 0

        # Expand the right edge and update window frequencies.
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            # Shrink while all required character types are satisfied.
            while have == need:
                if (r - l + 1) < res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return res
