from collections import deque

# LeetCode 907 - Sum of Subarray Minimums
# Approach 1: Brute Force (expand all subarrays)
# Time: O(n^2)
# Approach 2: Monotonic stack with sentinels
# Time: O(n)
# Approach 3: Previous/Next smaller element arrays
# Time: O(n)
# Space: O(n)

class Solution(object):
    def sumSubarrayMins(self, arr): # got TLE
        """
        :type arr: List[int]
        :rtype: int
        """
        # Brute force: compute minimum for every subarray starting at i.
        i = 0
        n = len(arr)
        res = 0
        while i < n:
            curr_min = arr[i]
            for j in range(i, n):
                curr_min = min(curr_min, arr[j])
                res += curr_min
            i += 1
            
        return res % (10**9 + 7)

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Use stack to find each value's contribution as subarray minimum.
        res = 0
        # Add sentinels to flush stack at both ends.
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = deque()
        
        for i in range(len(arr)):
            # Current value is next smaller for stack top values.
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                # Count choices on left and right where arr[j] is minimum.
                left = j - stack[-1]
                right = i - j
                res += arr[j] * left * right
            stack.append(i)
            
        return res % (10**9 + 7)

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Precompute nearest smaller indices on both sides.
        self.n = len(arr)
        def NextSmallerEle(arr):
            # nse[i] = index of next smaller element on right.
            nse = [-1] * self.n
            stack = deque()
            for i in range(self.n - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                nse[i] = self.n if not stack else stack[-1]
                stack.append(i)
            return nse

        def PrevSmallerEle(arr):
            # pse[i] = index of previous smaller element on left.
            pse = [-1] * self.n
            stack = deque()
            for i in range(self.n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                pse[i] = -1 if not stack else stack[-1]
                stack.append(i)
            return pse
                    
        nse = NextSmallerEle(arr)
        pse = PrevSmallerEle(arr)
        res = 0
        mod = 10**9 + 7
        
        # Contribution of arr[i] = arr[i] * choices_left * choices_right.
        for i in range(self.n):
            left = i - pse[i]
            right = nse[i] - i
            res += arr[i] * left * right
        
        return res % mod
