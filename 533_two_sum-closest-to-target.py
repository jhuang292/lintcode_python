class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return -1 
        nums.sort()
        diff = sys.maxsize
        
        l, r = 0, len(nums) - 1 
        while l < r:
            
            if nums[l] + nums[r] <= target:
                diff = min(diff, target - nums[l] - nums[r])
                l += 1 
            else:
                diff = min(diff, nums[l] + nums[r] - target)
                r -= 1
        return diff 
