class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
            
        nums.sort()
        counter = 0
        l, r = 0, len(nums) - 1 
        while l < r:
            if nums[l] + nums[r] <= target:
                l += 1 
            else:
                counter += r - l 
                r -= 1 
        return counter
