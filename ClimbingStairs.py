class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [None] * n
        steps[0:2] = [1, 2]
        for i in range(2, n):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n - 1]
