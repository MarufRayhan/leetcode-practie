class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_list = []
        empty_dict = {}
        for val in strs:
            sorted_value = ''.join(sorted(val))
            if sorted_value not in empty_dict:
                empty_dict[sorted_value] = [val]
            else:
                empty_dict[sorted_value].append(val)
        
        return list(empty_dict.values())



        