from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toArray(self):
        if self.next:
            return [self.val, *self.next.toArray()]

        return [self.val]


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        pivot = round(len(lists)/2)
        left = self.mergeKLists(lists[:pivot])
        right = self.mergeKLists(lists[pivot:])

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        res = temp = ListNode(0)

        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    temp.next = l2
                    l2 = l2.next
                else:
                    temp.next = l1
                    l1 = l1.next
            elif l1:
                temp.next = l1
                l1 = l1.next
            elif l2:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        return res.next
