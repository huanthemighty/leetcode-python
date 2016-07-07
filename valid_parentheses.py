class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True

        stack = []
        map = {'{': '}', '[': ']', '(': ')'}
        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if map.get(stack.pop()) != c:
                    return False

        return len(stack) == 0
