class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if Solution.overflow(x):
            return 0

        isNeg = x < 0
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x /= 10

        if isNeg:
            result = -result
        if Solution.overflow(result):
            return 0
        else:
            return result

    @staticmethod
    def overflow(x):
        return x >= 2 ** 31 or x < -(2 ** 31)
