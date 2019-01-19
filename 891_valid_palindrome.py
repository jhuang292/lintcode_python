class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        # Write your code here
        start, end = 0, len(s) - 1 
        while start < end:
            if s[start] == s[end]:
                start += 1 
                end -= 1 
            else:
                break
        if start >= end:
            return True
        return self.is_palindrome(s, start + 1, end) or self.is_palindrome(s, start, end - 1) 
        

    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1 
                end -= 1 
            else:
                return False
        return True
                
