# LeetCode 860 - Lemonade Change
# Approach: Greedy cash tracking
# Time: O(n)
# Space: O(1)

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # Track available $5 and $10 bills.
        map = {5: 0, 10: 0}
        for i in bills:
            # $5 bills are always added as change.
            if i == 5:
                map[5] += 1
            # For $10, we need one $5 as change.
            elif i == 10:
                map[10] += 1
                if map[5]:
                    map[5] -= 1
                else:
                    return False
            else:
                # Prefer one $10 + one $5 as change for $20.
                if map[10] and map[5]:
                    map[10] -= 1
                    map[5] -= 1
                # Otherwise use three $5 bills.
                elif map[5] >= 3:
                    map[5] -= 3
                else:
                    return False

        return True
