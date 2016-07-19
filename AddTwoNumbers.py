# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        node = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            node.next = ListNode(carry % 10)
            node = node.next
            carry /= 10

        if carry > 0:
            node.next = ListNode(carry)

        if dummy.next is None:
            return ListNode(0)
        else:
            return dummy.next
