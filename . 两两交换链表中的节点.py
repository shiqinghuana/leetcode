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

    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        f = head.next.next # 子链表
        q = head.next  # 第二个节点
        q.next = head # 第二个节点指向第一个节点
        head.next = self.swapPairs1(f)  #第一个节点指向下一个子链表
        return q


