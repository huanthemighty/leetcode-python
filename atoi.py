class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0

        is_neg = False
        index = 0
        if str[index] == '-':
            is_neg = True
            index += 1
        elif str[index] == '+':
            index += 1

        ret_val = 0
        for digit in xrange(index, len(str)):
            if not str[digit].isdigit():
                break
            else:
                ret_val *= 10
                ret_val += int(str[digit])

        if not is_neg and ret_val > 2147483647:
            return 2147483647
        elif is_neg and ret_val > 2147483648:
            return -2147483648

        if is_neg:
            return -ret_val
        else:
            return ret_val
