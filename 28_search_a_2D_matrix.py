class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or (len(matrix) == 0 and len(matrix[0]) == 0) or matrix[0][0] > target:
            return False
        
        nums = []
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                #nums = matrix[i]
                start, end = 0, len(matrix[i]) - 1 
                while start + 1 < end: 
                    mid = start + (end - start) // 2
                    if matrix[i][mid] < target:
                        start = mid
                    elif matrix[i][mid] > target:
                        end = mid
                    else: 
                        end = mid
                if matrix[i][start] == target:
                    return True
                elif matrix[i][end] == target:
                    return True
                else:
                    return False
        return False
