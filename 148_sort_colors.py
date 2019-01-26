class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        colors = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in colors:
                colors[nums[i]] = 1 
            else:
                colors[nums[i]] += 1 
        print(colors)
        
        for i in range(len(nums)):
            if colors[0] != 0 :
                nums[i] = 0
                colors[0] -= 1 
            else:
                if colors[1] != 0:
                    nums[i] = 1
                    colors[1] -= 1
                else:
                    if colors[2] != 0:
                        nums[i] = 2 
                        colors[2] -= 1 
                
                
        return nums
                
