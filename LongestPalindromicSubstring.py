# it's timing out for large dataset. probably need to use O(n) solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""

        table = [[False for x in range(1000)] for y in range(1000)]
        start = 0
        length = 1
        for i in range(n):
            table[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                length = 2

        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and table[i + 1][j - 1]:
                    table[i][j] = True
                    start = i
                    length = l

        return s[start:start + length]
