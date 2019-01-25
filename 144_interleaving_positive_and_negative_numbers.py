class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        if not A:
            return None
        if len(A) <= 2:
            return A 
        
        start, end = 0, len(A) - 1 
        while start < end:
            while start < end and A[start] < 0:
                start += 1 
            while start < end and A[end] > 0:
                end -= 1
            if start < end:
                A[start], A[end] = A[end], A[start]
                start += 1 
                end -= 1 
        neg_counter = start 
        pos_counter = len(A) - neg_counter 
        
        start = neg_counter - 1  
        end = neg_counter
        if abs(neg_counter - pos_counter) > 1:
            return 
        print(A)
        counter = 0
        if neg_counter == pos_counter:
            while counter < neg_counter // 2:
                A[start - 2 * counter - 1], A[end + 2 * counter + 1] = A[end + 2 * counter + 1], A[start - 2 * counter - 1] 
                counter += 1 
        elif neg_counter > pos_counter:
            while counter < neg_counter // 2:
                if neg_counter % 2 == 0:
                    A[start - 2 * counter], A[end + 2 * counter] = A[end + 2 * counter], A[start - 2 * counter] 
                    counter += 1
                else:
                    A[start - 2 * counter - 1], A[end + 2 * counter + 1] = A[end + 2 * counter + 1], A[start - 2 * counter - 1] 
                    counter += 1
        else:
            while counter < pos_counter // 2:
                if pos_counter % 2 == 0:
                    A[start - 2 * counter], A[end + 2 * counter] = A[end + 2 * counter], A[start - 2 * counter] 
                    counter += 1
                else:
                    A[start - 2 * counter - 1], A[end + 2 * counter + 1] = A[end + 2 * counter + 1], A[start - 2 * counter - 1] 
                    counter += 1
            
        return A
