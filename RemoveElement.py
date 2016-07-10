class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newlen = 0
        for n in nums:
            if n != val:
                nums[newlen] = n
                newlen += 1

        return newlen
