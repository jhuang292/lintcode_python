class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return None 
            
        pl, pr = 0, len(nums) - 1 
        i = 0
        
        while i <= pr:
            if nums[i] == 0:
                nums[pl], nums[i] = nums[i], nums[pl]
                i += 1 
                pl += 1 
            elif nums[i] == 1:
                i += 1 
            else:
                nums[pr], nums[i] = nums[i], nums[pr]
                pr -= 1 
