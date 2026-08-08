# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        ans = ListNode(0)
        cur = ans
        ct = 0
        for n in lists:
            if n:
                heapq.heappush(pq, (n.val, ct, n))
                ct += 1
        while pq:
            val, _, n = heapq.heappop(pq)
            cur.next = ListNode(val)
            n = n.next
            cur = cur.next
            if n:
                heapq.heappush(pq, (n.val, ct, n))
                ct += 1
        return ans.next