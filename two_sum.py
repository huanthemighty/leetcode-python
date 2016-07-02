class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_to_index = {}
        for i in range(len(nums)):
            if value_to_index.has_key(target - nums[i]):
                return value_to_index[target - nums[i]], i
            else:
                value_to_index[nums[i]] = i
