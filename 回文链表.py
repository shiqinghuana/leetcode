# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def get_mid( head: ListNode):
            slow , fast = head,head.next

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            p = slow.next
            slow.next = None
            return p

        def resver_list(head: ListNode):
            p = None
            while head:
                head.next,p,head = p,head,head.next
            return p
        if not head:
            return True
        mid = resver_list(get_mid(head))
        while head and mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True