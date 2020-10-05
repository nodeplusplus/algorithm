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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first, second = head, head.next
        remain = self.swapPairs(second.next)
        second.next = first
        first.next = remain
        return second


tests = [
    ([1, 2, 3, 4], [2, 1, 4, 3]),
]

for before_values, after_values in tests:
    before_node = None
    before_values.reverse()
    for before_value in before_values:
        before_node = ListNode(before_value, before_node)

    node = Solution().swapPairs(before_node)

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
