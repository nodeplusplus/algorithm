# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return (str(self.next) if self.next else '') + str(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2

        while True:
            t = cur1.val + cur2.val
            f = t % 10
            s = t//10

            cur1.val = f

            if not cur1.next and not cur2.next:
                if s > 0:
                    cur1.next = ListNode(s)
                break
            if not cur1.next:
                cur1.next = ListNode(0)
            if not cur2.next:
                cur2.next = ListNode(0)
            cur1 = cur1.next
            cur2 = cur2.next

            cur1.val += s

        return l1


first = ListNode(3)
first = ListNode(4, first)
first = ListNode(2, first)

second = ListNode(4)
second = ListNode(6, second)
second = ListNode(5, second)

# first = ListNode(5)
# second = ListNode(5)


# first = ListNode(1)
# second = ListNode(9)
# second = ListNode(9, second)

# first = ListNode(0)
# second = ListNode(3)
# second = ListNode(7, second)

# first = ListNode(9)
# first = ListNode(9, first)
# second = ListNode(9)


print(Solution().addTwoNumbers(first, second), '###')
