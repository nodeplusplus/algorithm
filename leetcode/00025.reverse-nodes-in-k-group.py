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
    def reverseKGroup(self, head: ListNode, k: int, c=0) -> ListNode:
        if k == 1 or not head or not head.next:
            return head

        if not c:
            t = head
            while t:
                t = t.next
                c += 1

        if c < k:
            return head

        i, j, n = None, head, 0
        while j and n < k:
            t = j.next
            j.next = i
            i, j = j, t
            n += 1

        head.next = self.reverseKGroup(j, k, c-k)

        return i


tests = [
    # ([[1, 2, 3, 4, 5], 3], [3, 2, 1, 4, 5]),
    ([[1, 2, 3], 3], [3, 2, 1]),
    ([[1, 2, 3, 4], 4], [4, 3, 2, 1]),
]

for [before_values, k], after_values in tests:
    before_node = None
    before_values.reverse()
    for before_value in before_values:
        before_node = ListNode(before_value, before_node)

    node = Solution().reverseKGroup(before_node, k)

    after_node = None
    after_values.reverse()
    for after_value in after_values:
        after_node = ListNode(after_value, after_node)

    if not node and not after_node:
        print(f"\033[92m -> OK")
    elif node.toArray() != after_node.toArray():
        print(f"\033[91m -> {node.toArray()} # {after_node.toArray()}")
    else:
        print(f"\033[92m -> OK")
