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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return None

        res = head
        node = None
        skip = -n
        while head.next:
            skip += 1
            head = head.next
            if node:
                node = node.next
            if skip == 0:
                node = res
            if not head.next:
                # remove latest node
                if not node:
                    res = res.next
                else:
                    node.next = node.next.next

        return res


# # Shorter
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         res = ListNode(0)
#         res.next = head
#         i = j = res

#         # if n = 2
#         # 0 1 2 3
#         # i _ j
#         for _ in range(n+1):
#             j = j.next

#         while j:
#             i = i.next
#             j = j.next

#         i.next = i.next.next
#         return res.next


tests = [
    ([[1, 2, 3, 4, 5], 2], [1, 2, 3, 5]),
    ([[1, 2], 1], [1]),
    ([[1], 1], []),
    ([[1, 2], 2], [2]),
]

for [node_values, index],  r in tests:
    node = None
    node_values.reverse()
    for node_value in node_values:
        node = ListNode(node_value, node)
    a = Solution().removeNthFromEnd(node, index)

    head = None
    r.reverse()
    for value in r:
        head = ListNode(value, head)

    if not a and not head:
        print(f"\033[92m -> OK")
    elif a.toArray() != head.toArray():
        print(f"\033[91m -> {a.toArray()} # {head.toArray()}")
    else:
        print(f"\033[92m -> OK")
