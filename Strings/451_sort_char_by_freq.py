"""
LeetCode 451 - Sort Characters By Frequency
Approach:
- Use `collections.Counter` to count the frequency of each character in the string.
- Sort the dictionary items by their frequency values in descending order.
- Reconstruct the string by multiplying each character by its frequency and appending to a result string.
Time: O(N) since the number of unique characters is bounded by the alphabet/ASCII size, sorting takes O(1) effectively.
Space: O(N) to store the result string and the character frequencies.
"""

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the frequency of each character
        cnt = Counter(s)
        s=""
        
        # Sort the characters based on frequency in descending order
        cnt = sorted(cnt.items(),key= lambda x:x[1],reverse=True)
        
        # Reconstruct the string
        for c in cnt:
            # c[0] is the character, c[1] is its frequency
            s+= c[0]*c[1]
        return s