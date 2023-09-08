from collections import deque

def solve(que: deque, ans: list) -> None:
    flag = True  # True -> left to right // False -> right to left

    while que:
        size = len(que)
        temp = [None]*size

        for i in range(size):
            node = que.popleft()

            index = i if flag else size - i - 1

            temp[index] = node.val

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        flag = not flag

        ans.append(temp)


if __name__ == "__main__":
    ans = []
    q = deque(["root"])
    solve(q)
