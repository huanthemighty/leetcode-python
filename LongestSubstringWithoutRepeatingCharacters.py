class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        has = [False] * 256

        has[ord(s[0])] = True
        start = 0
        result = 1

        for end in range(1, len(s)):
            if has[ord(s[end])]:
                result = max(result, end - start)
                while start < end and s[start] != s[end]:
                    has[ord(s[start])] = False
                    start += 1
                if start < end:
                    start += 1
            else:
                has[ord(s[end])] = True

        return max(result, len(s) - start)
