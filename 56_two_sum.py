class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i, a in enumerate(numbers):
            for j, b in enumerate(numbers[i + 1 - len(numbers):]):
                if a + b == target:
                    return [i, i + 1 + j]
        return [-1, -1]
