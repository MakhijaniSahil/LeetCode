# LeetCode 402 - Remove K Digits
# Approach: Monotonic increasing stack (greedy removal)
# Time: O(n)
# Space: O(n)


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # If k is larger than number length, smallest value is 0.
        if k >= len(num):
            return "0"

        # Stack stores digits in increasing order.
        res = ""
        stack = []
        for n in num:
            # Remove larger previous digits to get smaller lexicographic number.
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            stack.append(n)

        # If removals remain, remove from end (largest remaining suffix).
        while stack and k:
            stack.pop()
            k -= 1

        # Remove leading zeros from the constructed answer.
        res = "".join(stack).lstrip("0")

        # Return 0 if all digits were removed or trimmed.
        return res if res else "0"
