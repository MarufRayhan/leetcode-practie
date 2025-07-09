class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        empty_dict = {}
        max_key = str(0)
        for num in nums:
            max_key = max(str(num))
            
            if max_key not in empty_dict:
                empty_dict[max_key] = [num]
            else:
                empty_dict[max_key].append(num)
    
        max_sum = -1
        for key, number_list in empty_dict.items(): 
            if len(number_list) >= 2:
                number_list.sort(reverse=True)  
                max_result = number_list[0]+number_list[1]
                max_sum = max(max_sum, max_result)

        return max_sum
                
        