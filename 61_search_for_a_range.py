class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1,-1]
            
        bound = []
        
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if A[mid] < target:
                start = mid 
            elif A[mid] > target:
                end = mid 
            else:
                end = mid
        if A[start] == target:
            bound.append(start)
        elif A[end] == target:
            bound.append(end)
        else:
            return [-1,-1]
            
        start, end = 0, len(A) -1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid
        if A[end] == target:
            bound.append(end)
        elif A[start] == target:
            bound.append(start)
        else:
            return [-1,-1]
        
        return bound
