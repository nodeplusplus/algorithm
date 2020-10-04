# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toArray(self):
        if self.next:
            return [self.val, *self.next.toArray()]

        return [self.val]


class Solution:
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


tests = [
    ([[1, 2, 4], [1, 3, 4]], [1, 1, 2, 3, 4, 4]),
    # ([[1], []]5]),
]

for [l1_values, l2_values],  r in tests:
    l1_values.reverse()
    l1 = None
    for l1_value in l1_values:
        l1 = ListNode(l1_value, l1)

    l2_values.reverse()
    l2 = None
    for l2_value in l2_values:
        l2 = ListNode(l2_value, l2)

    head = None
    r.reverse()
    for value in r:
        head = ListNode(value, head)

    a = Solution().mergeTwoLists(l1, l2)

    if not a and not head:
        print(f"\033[92m -> OK")
    elif a.toArray() != head.toArray():
        print(f"\033[91m -> {a.toArray()} # {head.toArray()}")
    else:
        print(f"\033[92m -> OK")
