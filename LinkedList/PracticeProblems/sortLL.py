class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortList(head):
    # Write your code here
    zero_head, one_head, two_head = Node(-1), Node(-1), Node(-1)

    zero, one, two = zero_head, one_head, two_head

    temp = head

    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next

        temp = temp.next

    zero.next = one_head.next if one_head.next else two_head.next
    one.next = two_head.next
    two.next = None

    return zero_head.next
