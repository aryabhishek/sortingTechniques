def solution(prices: list) -> int: # TC: O(n), SC: O(1)

    mini = prices[0]
    max_profit = 0

    n = len(prices)

    for i in range(1, n):
        cost = prices[i] - mini
        max_profit = max(max_profit, cost)
        mini = min(mini, prices[i])

    return max_profit


if __name__ == "__main__":
    arr = [7,1,5,3,6,4]

    print(solution(arr))