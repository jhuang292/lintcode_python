class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.quickSort(A, 0, len(A) - 1)
        
    def quickSort(self, nums, start, end):
        if start > end:
            return 
            
        i, j = start, end 
        pivot = nums[(i + j) // 2]
        
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1 
            while i <= j and nums[j] > pivot:
                j -= 1 
            if i <= j: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 
                j -= 1 
        self.quickSort(nums, start, j)
        self.quickSort(nums, i, end)
