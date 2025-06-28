class Solution:
    def climbStairs(self, n: int) -> int:
        x = [1, 1]

        for i in range(1, n):
            x.append(x[i-1] + x[i])

        return x[-1]
