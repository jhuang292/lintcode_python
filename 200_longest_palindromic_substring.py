class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        longest = ""
        for middle in range(len(s)):
            sub = self.find_palindrome_from(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub

        return longest
        
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
            
        return string[left + 1:right]
