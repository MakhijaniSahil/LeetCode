"""
LeetCode 3514 - Number of Unique XOR Triplets II
Approach 1: Brute Force with Sets
- Enumerate all pair XORs, then combine them with every array value.
- Store results in a set to deduplicate triplet XOR values.
- This approach is correct but too slow for large inputs.
Time: TLE
Space: O(n^2)

Approach 2: Boolean Arrays
- Compute the maximum possible XOR range from the largest input value.
- Mark reachable pair XORs and then reachable triplet XORs with boolean arrays.
- Count how many triplet XOR values were reached.
Time: O(n^3) in the worst case, but faster in practice with array lookups
Space: O(maxXor)
"""

class Solution(object): # Got TLE
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Collect every distinct XOR value formed by two numbers.
        pairXor = set()

        for i in nums:
            for j in nums:
                pairXor.add(i ^ j)

        # Combine pair XORs with every number to form triplet XORs.
        triplet = set()

        for i in pairXor:
            for j in nums:
                triplet.add(i ^ j)

        return len(triplet)


class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Build the maximum XOR range we may need to track.
        n = len(nums)
        maxNum = max(nums)

        maxXor = 1
        while maxXor <= maxNum:
            maxXor <<= 1

        # Boolean arrays mark reachable XOR values.
        pairXor = [False] * maxXor
        tripletXor = [False] * maxXor

        # Mark all pair XOR results.
        for i in nums:
            for j in nums:
                pairXor[i ^ j] = True

        # Expand every reachable pair XOR with each number to form triplets.
        for i in range(maxXor):
            if pairXor[i]:
                for j in nums:
                    tripletXor[i ^ j] = True

        # Count the triplet XOR values that were reached.
        cnt = 0

        for i in tripletXor:
            if i:
                cnt += 1

        return cnt
