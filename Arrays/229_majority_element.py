"""
LeetCode 229 - Majority Element II
Approach:
- Use a variant of the Boyer-Moore Voting Algorithm.
- Maintain a dictionary to track up to 2 potential majority candidates and their counts.
- When a 3rd distinct element is encountered, decrement the counts of all currently tracked candidates.
- In a second pass, verify if the remaining candidates actually appear more than ⌊n/3⌋ times.
Time: O(n)
Space: O(1) (the dictionary size never exceeds 2)
"""

from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Dictionary to store at most 2 candidate elements and their frequencies.
        count = defaultdict(int)

        for num in nums:
            # Increment the count for the current number.
            count[num]+=1

            # If we have 2 or fewer candidates, we don't need to decrement anything.
            if len(count)<=2:
                continue

            # If we exceed 2 candidates, decrement all counts by 1.
            new_count = defaultdict(int)
            for n,c in count.items():
                if c>1:
                    new_count[n]=c-1

            # Update the candidates.
            count = new_count

        res = []
        # Second pass to verify if the candidates actually meet the > n/3 requirement.
        for n in count:
            if nums.count(n)>(len(nums)//3):
                res.append(n)
        
        return res