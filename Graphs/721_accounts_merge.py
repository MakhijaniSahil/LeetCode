"""
LeetCode 721 - Accounts Merge
Approach:
- Treat each account as a node in a union-find structure.
- Union accounts that share at least one email address.
- Collect emails by connected component and sort them for the final merged account.
Time: O(n * m * alpha(n))
Space: O(n * m)
"""

from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # Number of accounts.
        n = len(accounts)
        if n == 1:
            return accounts

        # Union-find parent and size/rank arrays.
        parent = [i for i in range(n)]
        rank = [0] * n

        # Find the root account with path compression.
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # Merge two accounts if they share an email.
        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return False

            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]

            return True

        # Map each email to the first account index that contained it.
        emailToAcc = {}

        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e in emailToAcc:
                    union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        # Group all emails by the final union-find leader.
        emailGroup = defaultdict(list)

        for e, i in emailToAcc.items():
            leader = find(i)
            emailGroup[leader].append(e)

        # Build the merged account list with sorted emails.
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res
