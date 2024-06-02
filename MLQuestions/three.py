# There are N cities in a country. George is initially at the airport in city 1 and he wants to reach city N. For any city i, there is either a flight to city (i+1) or to (i+3) if it exists.
# You have been given an array A with the costs of flight tickets for N cities. To find the cost of a flight ticket between any two cities i and j, you take the absolute difference of the costs of those cities in the array A. You can use the formula |a| = |Cost[i] - Cost[j]] to calculate the cost of a flight ticket, where [al represents the absolute value of a.

# Your task is to find and return the minimum possible cost of flight ticket required to reach the city N.

# Note:
# •	The number of cities is always greater than 3.
# •	Assume 1 based indexing.

# Input Specification:
# input1: An integer value N, representing the number of cities.
# input2: An integer array A, representing the cost of tickets to reach the ith a city.

# Output Specification:
# Return the minimum possible cost of flight ticket required to reach the city N.

# Example 1:
# input1: 4
# input2: (1,4,5,2)

# Output: 1 Explanation:
# George takes a flight in the below optimal manner:
# •	From city 1 to city 4, as city 4 is the third next city to city 1 so the cost will be |1-2|=1.
# Hence, 1 is returned as the output.

# Example 2:
# input1: 6
# input2 (4,12,13,18,10,12)
# Output: 10

# Explanation:
# George takes a flight in the below optimal manner: From city 1 to city 2, the cost will be |4- 12| = 8
# •	From city 2 to city 3, the cost will be |12-13| = 1
# . From city 3 to city 6, the cost will be |13-12| = 1
# Therefore, the total cost is 8 + 1 + 1 = 10. Hence, 10 is returned as the output.


def solve(i, n, arr, memo):
    if i == n:
        return 0
    if i in memo:
        return memo[i]
    cost = float("inf")
    if i + 1 <= n:
        cost = min(cost, abs(arr[i - 1] - arr[i]) + solve(i + 1, n, arr, memo))
    if i + 3 <= n:
        cost = min(cost, abs(arr[i - 1] - arr[i + 2]) + solve(i + 3, n, arr, memo))
    memo[i] = cost
    return cost

def tabulation(n, arr):
    dp = [float("inf")] * (n + 1)
    dp[1] = 0

    for i in range(1, n):
        if i + 1 <= n:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(arr[i - 1] - arr[i]))
        if i + 3 <= n:
            dp[i + 3] = min(dp[i + 3], dp[i] + abs(arr[i - 1] - arr[i + 2]))

    return dp[n]

if __name__ == "__main__":
    n = 6
    arr = [4, 12, 13, 18, 10, 12]
    print(solve(1, n, arr, {}))
    print(tabulation(n, arr))
