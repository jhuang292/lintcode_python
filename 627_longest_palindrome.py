class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        counter = 0
        for v in collections.Counter(s).values():
            counter += v // 2 * 2
            if (counter % 2 == 0 and v % 2 == 1):
                counter += 1
        return counter
