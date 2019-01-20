class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
        
        nums.sort()
        
        counter = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                counter, l, r = counter + 1, l + 1, r - 1 
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1 
                while l < r and nums[l] == nums[l - 1]:
                    l += 1 
            elif nums[l] + nums[r] < target:
                l += 1 
            else:
                r -= 1 
        return counter
