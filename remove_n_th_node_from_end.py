# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        runner = head
        for i in range(n):
            runner = runner.next

        follower = head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        last = dummy_head
        while runner is not None:
            runner = runner.next
            follower = follower.next
            last = last.next

        last.next = follower.next
        return dummy_head.next
