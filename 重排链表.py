# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        l = []
        while head:
            l.append(head)
            head = head.next
        while len(l)>2:
            first = l.pop(0)
            last = l.pop()
            first.next = last
            last.next = l[0]
        l[-1].next = None


    def reorderList2(self, head: ListNode) -> None:


        # 1:拿到中点
        def get_mid(head: ListNode):
            fast,slow = head,head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            p = slow.next # 此处，以slow为中点分成左右两个子链表
            slow.next = None
            return p

        # 2：翻转链表

        def resverList(head: ListNode):
            q =None

            while head:
                head.next,q,head =q, head,head.next

            return q

        # 3: 把左右两个链表串起来
        if not head:
            return
        mid = get_mid(head)
        nw = resverList(mid)

        while head and nw:
            p = head.next
            q = nw.next

            head.next = nw
            nw.next = p

            head = p
            nw = q


    def reorderList1(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        """
        对任一子链表，都有  首节点-> 尾结点
        
        直到 链表长度 <2 
        结束递归
        """

        if not head or not head.next or not head.next.next:
            return
        p=head
        first = head.next

        last = None

        while p:
            if not p.next.next:
                last = p.next
                p.next = None
                break
            p = p.next
        head.next = last
        last.next = first
        self.reorderList(first)