from collections import deque

# LeetCode 735 - Asteroid Collision
# Approach 1: Stack with sign/magnitude tuples
# Time: O(n)
# Approach 2: Stack for right-movers + result for settled left-movers
# Time: O(n)
# Space: O(n)


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # Final surviving asteroids in original order.
        res = []
        # Stack stores (direction_bit, magnitude): 0 => right, 1 => left.
        stack = deque()
        for a in asteroids:
            # Determine direction and normalize magnitude.
            sign_bit = 0
            if a < 0:
                sign_bit = 1

            # Resolve collisions: incoming left-mover destroys smaller right-movers.
            while stack and sign_bit and not stack[-1][0] and abs(a) > stack[-1][1]:
                stack.pop()

            # If opposite directions still meet, handle equal-size annihilation.
            if stack and sign_bit and not stack[-1][0]:
                if abs(a) == stack[-1][1]:
                    stack.pop()
            else:
                # No collision, so asteroid survives for now.
                stack.append((sign_bit, abs(a)))
            print(stack)

        # Rebuild signed values from stack tuples.
        while stack:
            bit, val = stack.popleft()
            if bit:
                res.append(-val)
            else:
                res.append(val)

        return res


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # res collects left-moving asteroids that can never collide again.
        res = []
        # stack keeps only right-moving asteroids not yet destroyed.
        stack = []
        for a in asteroids:
            if a < 0:
                # Destroy smaller right-movers while collision is possible.
                while stack and abs(a) > stack[-1]:
                    stack.pop()
                # No right-movers left, current left-mover survives.
                if not stack:
                    res.append(a)
                # Equal sizes destroy each other.
                if stack and stack[-1] == -a:
                    stack.pop()
            else:
                # Right-movers are pushed for future collision checks.
                stack.append(a)

            print(res, stack)

        # Remaining right-movers survive and appear after settled left-movers.
        res += stack
        return res
