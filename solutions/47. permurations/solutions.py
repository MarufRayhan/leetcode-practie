class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.permute(nums)
    
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        result = []
        for i in range (len(nums)):
            fixed_first = nums[i]
            
            remaining  = nums[:i] + nums[i+1:]

            if i > 0 and nums[i] == nums [i-1]:
                continue
            sub_perms = self.permuteUnique(remaining)

            for perms in sub_perms:
                result.append([fixed_first] + perms)
        return result


        