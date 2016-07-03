class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digit = self.getDigit(x)
        while x > 0:
            r = x % 10
            l = x / 10 ** (digit - 1)
            if l != r:
                return False
            x -= l * 10 ** (digit - 1)
            x /= 10
            digit -= 2
        return True


    def getDigit(self, x):
        """
        count the digit of the positive integer
        :param x: int
        :return: int
        """
        d = 0
        while x > 0:
            d += 1
            x /= 10
        return d