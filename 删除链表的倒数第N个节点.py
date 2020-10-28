# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        p = head

        l = []

        while head:
            l.append(head)
            head = head.next

        if n == len(l):
            return p.next
        if n==1:
            l[-2].next = None
            return p
        l[-n-1].next = l[-n+1]
        return p

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:

        p = f = ListNode(0, head)
        k = 0
        while head:
            if k >= n:
                f = f.next
            head = head.next
            k += 1
        f.next = f.next.next
        return p.next
