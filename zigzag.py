import operator

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        liststr = [''] * numRows
        down = True
        ind = 0
        for i in range(len(s)):
            liststr[ind] += s[i]
            if ind == numRows - 1:
                down = False
            elif ind == 0:
                down = True

            if down:
                ind += 1
            else:
                ind -= 1
            ind %= numRows

        return reduce(operator.add, liststr)