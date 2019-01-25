class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        if not chars:
            return None
        
        i, j = 0, len(chars) - 1 
        while i < j:
            while i < j and chars[i].islower():
                i += 1 
            while i < j and chars[j].isupper():
                j -= 1 
            if i < j:
                temp = chars[i]
                chars[i] = chars[j]
                chars[j] = temp
                i += 1 
                j -= 1 
        return chars
