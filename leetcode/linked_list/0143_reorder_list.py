# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        k = []
        p = head
        while p:
            k.append(p.val)
            p = p.next

        l = []
        t = 0
        
        for i in range(len(k)):
            if(i % 2 == 1):
                l.append(k[len(k)-1-t])
                t += 1
            if(i % 2 == 0):
                l.append(k[i//2])                
        he = head
        i = 0
        while he:
            he.val = l[i]
            he = he.next
            i+= 1
        
        """
        Do not return anything, modify head in-place instead.
        """
        