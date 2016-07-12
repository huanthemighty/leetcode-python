class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        all_nine = True
        for d in digits:
            if d != 9:
                all_nine = False
                break

        if all_nine:
            result = [0] * (len(digits) + 1)
            result[0] = 1
            return result

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            else:
                sum = digits[i] + carry
                digits[i] = sum % 10
                carry = sum / 10

        return digits
