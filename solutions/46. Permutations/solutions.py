class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]
        result = []
        for i in range(len(nums)):
            fixed_first = nums[i]

            remaining_values = nums[:i] + nums[i+1:]
            sub_perms = self.permute(remaining_values)

            for perms in sub_perms:
                result.append([fixed_first] + perms)
        return result

        