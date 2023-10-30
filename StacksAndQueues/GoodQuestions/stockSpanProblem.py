from collections import deque


def solution(arr, n) -> list:
    stk = deque()
    res = []
    
    for i in range(n):
        
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        if not stk:
            res.append(i+1) # edge case: what if the last element is greater than every other? or the stack gets emptied??

        else:
            res.append(i-stk[-1])

        stk.append(i)

    return res


if __name__ == "__main__":
    price = [100, 80, 60, 70, 60, 75, 101]
    print(solution(price, len(price)))
