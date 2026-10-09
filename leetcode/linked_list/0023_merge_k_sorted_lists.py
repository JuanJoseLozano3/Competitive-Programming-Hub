import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        for i in lists:
            head = i
            while head:
                heapq.heappush(heap, head.val)
                head = head.next

        if not heap:
            return None
        
        nueva = ListNode()
        actual = nueva
        for i in range(len(heap)):
            actual.val = heapq.heappop(heap)
            if heap:
                actual.next = ListNode()
                actual = actual.next
        
        return nueva
