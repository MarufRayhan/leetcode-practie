class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        for char in s:
            if char not in dict1:
                dict1[char] = 0
            dict1[char] += 1
        dict2 = {}
        for char in t:
            if char not in dict2:
                dict2[char] = 0
            dict2[char] += 1 
        
        return dict1==dict2
                
        