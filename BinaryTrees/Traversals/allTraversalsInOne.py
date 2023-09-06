from collections import deque


def get_all_traversals(root, pre_order: list, in_order: list, post_order: list) -> None:
    stk = deque()
    stk.append([root, 1])

    if not root:
        return

    while stk:
        item = stk[-1]
        stk.pop()

        if item[1] == 1:
            pre_order.append(item[0].val)
            item[1] += 1
            stk.append(item)

            if item[0].left:
                stk.append([item[0].left, 1])

        elif item[1] == 2:
            in_order.append(item[0].val)
            item[1] += 1
            stk.append(item)

            if item[0].right:
                stk.append([item[0].right, 1])

        else:
            post_order.append(item[0].val)
