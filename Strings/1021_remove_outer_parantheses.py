"""
LeetCode 1021 - Remove Outermost Parentheses
Approach:
- Use a counter (`open_cnt`) to track the depth of the nested parentheses.
- Iterate through each character in the string.
- When encountering an open parenthesis `(`, it's part of the inner string if `open_cnt > 0`. We append it to the result and then increment the depth.
- When encountering a close parenthesis `)`, we first decrement the depth. If the depth is still `> 0`, it means it's an inner parenthesis, so we append it to the result.
Time: O(N)
Space: O(N) to build the result string
"""

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Track the depth of parentheses.
        open_cnt = 0
        res = ""
        
        for c in s:
            if c=='(':
                # If depth > 0, this is not the outermost '('.
                if open_cnt>0:
                    res+=c
                open_cnt+=1

            if c==')':
                open_cnt-=1
                # If depth > 0 after decrement, this is not the outermost ')'.
                if open_cnt>0:
                    res+=c
                    
        return res