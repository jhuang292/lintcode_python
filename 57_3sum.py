class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        result = []
        length = len(numbers)
        
        for i in range(length - 2):
            if numbers[i] == numbers[i - 1]:
                continue
            target = -numbers[i]
            l, r = i + 1, length - 1 
            while l < r:
                if numbers[l] + numbers[r] == target:
                    result.append([numbers[i], numbers[l], numbers[r]])
                    l += 1 
                    r -= 1 
                    while l < r and numbers[l] == numbers[l - 1]:
                        l += 1 
                    while l < r and numbers[r] == numbers[r + 1]:
                        r -= 1 
                elif numbers[l] + numbers[r] < target:
                    l += 1 
                else:
                    r -= 1 
        return result
