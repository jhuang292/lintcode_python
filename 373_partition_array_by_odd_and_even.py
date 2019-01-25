class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if not nums:
            return None
        
        start, end = 0, len(nums) - 1 
        while start < end:
            while start < end and nums[start] % 2 == 1:
                start += 1 
            while start < end and nums[end] % 2 == 0:
                end -= 1 
            if start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1 
                end -= 1 
        return nums
