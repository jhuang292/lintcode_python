class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        # look for A[left] < target, A[right] >= target
        # look for the two values which are the closest to target
        right = self.find_upper_closest(A, target)
        left = right - 1 
        
        # two pointers start from the mid and count for the k values
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1 
            else:
                results.append(A[right])
                right += 1 
        return results
        
        
        
    def find_upper_closest (self, A, target):
        # find the first number >= target in A 
        start, end = 0, len(A) - 1
        while start + 1 < end: 
            mid = start + (end - start) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
                
        if A[start] >= target:
            return start
        
        if A[end] >= target:
            return end 
            
        # Cannot find the contion
        return end + 1 
        
    def is_left_closer (self, A, target, left, right):
        # First two condtion to control the range of the left and right
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
