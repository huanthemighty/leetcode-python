from collections import deque

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = deque()
        carry = 0
        for i in range(max(len(a), len(b))):
            if i < len(a) and a[len(a) - 1 - i] == '1':
                carry += 1
            if i < len(b) and b[len(b) - 1 - i] == '1':
                carry += 1

            result.appendleft(str(carry % 2))
            carry /= 2

        if carry > 0:
            result.appendleft('1')

        return ''.join(result)
