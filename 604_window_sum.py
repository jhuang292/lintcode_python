class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if k > len(nums) or not nums:
            return []
        
        result = []
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        result.append(sum)
        
        m = 0
        for j in range(k, len(nums)):
            sum = sum + nums[j] - nums[m]
            result.append(sum)
            m += 1 
        return result
