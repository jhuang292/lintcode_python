class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return -1
        
        l, r = 0, len(nums) -1
        for i in range(r):
            while l < r and nums[l] + nums[r] < target:
                l += 1 
            if l != r and nums[l] + nums[r] == target:
                return [l+1, r+1]
            r -= 1
        return -1
