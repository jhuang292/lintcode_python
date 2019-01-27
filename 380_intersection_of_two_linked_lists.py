"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        lenA, lenB = 0, 0
        node1, node2 = headA, headB
        
        while node1 is not None:
            node1 = node1.next
            lenA += 1 
        while node2 is not None:
            node2 = node2.next
            lenB += 1 
        
        node1, node2 = headA, headB
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1 
        while lenB > lenA:
            node2 = node2.next
            lenB -= 1 
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
            lenA -= 1 
            lenB -= 1 
        return node1
