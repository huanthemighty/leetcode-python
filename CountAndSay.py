class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        prev = self.countAndSay(n - 1)
        result = ''
        repeatedness = 1
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                repeatedness += 1
            else:
                result += str(repeatedness)
                result += prev[i - 1]
                repeatedness = 1

        result += str(repeatedness)
        result += prev[len(prev) - 1]
        return result
