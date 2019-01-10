class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s = ''.join([el.lower() for el in s if el and el.isalnum()])
        start, end = 0, len(s)-1
        while start<end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
