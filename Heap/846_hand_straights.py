import heapq

# LeetCode 846 - Hand of Straights
# Approach 1: Min Heap + Temporary Buffer
# Time: O(n log n)
# Space: O(n)
#
# Approach 2: Sort + Backward Scan 
# Time: O(n^2) in worst case because of pop(j)
# Space: O(1) extra

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if(n%groupSize!=0):
            return False
        heapq.heapify(hand)  # always pick smallest available card
        q = []  # store cards that cannot be used in current group
        prev = 0
        groups = n // groupSize  # total groups we must form
        cur_len = 0  # length of current consecutive group
        while hand and groups:
            h = heapq.heappop(hand)
            if(not cur_len):
                prev = h
                cur_len+=1
            elif(h==prev+1):
                prev=h
                cur_len+=1
            else:
                q.append(h)

            if(cur_len==groupSize):
                groups-=1
                cur_len=0
                # push skipped cards back for next group
                while q:
                    heapq.heappush(hand,q.pop())

        return False if groups else True


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        hand.sort()  # sort once and build groups from largest card
        groups = n // groupSize  # total groups to form

        for _ in range(groups):
            curr_num = hand.pop()  # largest remaining card starts group
            curr_len = 1
            j = len(hand) - 1  # scan backward for next smaller needed card
            while curr_len < groupSize:
                # skip duplicates of current value while scanning
                while j >= 0 and hand[j] == curr_num:
                    j -= 1
                # next card must be exactly current - 1
                if j < 0 or hand[j] != curr_num - 1:
                    return False
                curr_num = hand.pop(j)
                curr_len += 1
                j -= 1

        return not hand  # all cards used successfully