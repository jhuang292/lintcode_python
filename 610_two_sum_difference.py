class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)
        n, indexes = len(nums), []
        nums = sorted(nums, key=lambda x: x[0])
        
        j = 0
        for i in range(n):
            if i == j:
                j += 1 
                
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1 
            if j < n and nums[j][0] - nums[i][0] == target:
                indexes = [nums[i][1] + 1, nums[j][1] + 1]
                
        if indexes[0] > indexes[1]:
            return [indexes[1], indexes[0]]
        return indexes    
            
        
