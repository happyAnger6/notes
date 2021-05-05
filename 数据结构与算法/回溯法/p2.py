# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_number(l1, l2):
    def add_list(l1, l2, carry=0, tail=None):
        if l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            num = val % 10
            carry = val//10
            node = ListNode(num)
            tail.next = node
            tail = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            add_list(l1, l2, carry, tail)
        else:
            if carry != 0:
                node = ListNode(carry)
                tail.next = node
                tail = node
            return tail

    dummy = ListNode(-1)
    add_list(l1, l2, 0, dummy)
    return dummy.next