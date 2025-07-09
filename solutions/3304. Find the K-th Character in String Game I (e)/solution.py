class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        def next_char(c):
            return "a" if c == "z" else chr(ord(c)+1)

        word = "a"

        while (len(word) < k):
            next_part = ''.join(next_char(char) for char in word)
            word +=next_part
        return word[k-1]

        