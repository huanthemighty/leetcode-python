class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ''
        for index in range(0, len(strs[0])):
            c = strs[0][index]
            for j in range(1, len(strs)):
                if index >= len(strs[j]) or c != strs[j][index]:
                    return strs[0][0:index]
        return strs[0]
