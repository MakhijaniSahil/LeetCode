"""
LeetCode 17 - Letter Combinations of a Phone Number
Approach: Backtracking over the keypad mapping
Time: O(4^n) in the worst case
Space: O(n)
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Digit-to-letters mapping for a phone keypad
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        path = []

        def backtrack(i, path):
            # When we have processed every digit, record the current combination
            if i >= len(digits):
                res.append("".join(path))
                return

            # Try every possible letter for digits[i]
            for c in map[digits[i]]:
                path.append(c)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, path)
        return res