class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1 
            
        i, values_dic =0, {}
        for item in nums:
            if item not in values_dic:
                values_dic[item] = 1 
                nums[i] = item 
                i += 1 
        return i 
