# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""

        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        s2 = ""
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        all = f"{s1[::-1]}+{s2[::-1]}"
        all1 = str(eval(all))[::-1]
        p = k = ListNode(None)
        for i in all1:
            p.next = ListNode(int(i))
            p = p.next
        return k.next