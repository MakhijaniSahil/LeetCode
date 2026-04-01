# LeetCode 455 - Assign Cookies
# Approach: Greedy (Sort and Two Pointers)
# Time: O(nlogn + mlogm) where n = len(g), m = len(s)
# Space: O(1)

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Sort both lists to maximize content children
        g.sort()
        s.sort()
        i = len(g) - 1  # pointer for children (greed)
        j = len(s) - 1  # pointer for cookies (size)
        count = 0  # number of content children
        # Iterate from the end (largest greed and largest cookie)
        while(i >= 0 and j >= 0):
            if(g[i] <= s[j]):  # if cookie can satisfy child
                count += 1     # assign cookie
                j -= 1        # move to next largest cookie
            i -= 1            # move to next child
        # Return total content children
        return count