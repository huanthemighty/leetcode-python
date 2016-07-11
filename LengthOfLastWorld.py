class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_char_index = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if last_char_index > 0:
                    return last_char_index - i
            elif last_char_index == -1:
                last_char_index = i

        if last_char_index == -1:
            return 0
        else:
            return last_char_index + 1
