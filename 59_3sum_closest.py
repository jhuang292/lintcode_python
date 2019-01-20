class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 3:
            return -1
            
        numbers.sort()
        ans = None 
         
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1 
            while l < r:
                sum_value = numbers[l] + numbers[r] + numbers[i]
                if ans is None or abs(sum_value - target) < abs(ans - target):
                    ans = sum_value
                if sum_value < target:
                    l += 1 
                else:
                    r -= 1 
        return ans
