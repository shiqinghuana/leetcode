# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        l= []
        while head :
            if len(l)%2==0:
                l.append(head)
            else:
                l.insert(-1,head)
            head = head.next
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next =None
        return l[0]
