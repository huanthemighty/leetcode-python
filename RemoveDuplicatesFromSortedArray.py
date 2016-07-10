class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        newlen = 1
        for pos in range(1, len(nums)):
            if nums[pos] != nums[newlen - 1]:
                nums[newlen] = nums[pos]
                newlen += 1

        return newlen
