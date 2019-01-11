class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        start, end = 0, len(nums)-1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if (nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]):
                start = mid
            elif (nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]):
                end = mid
            else:
                return nums[mid]
                
        if (nums[start] > nums[end]):
            return nums[start]
        else:
            return nums[end]
