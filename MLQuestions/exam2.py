def last_chocolate(i, j, k, memo):
    if i == j == k:
        return 1
    
    if i > j or i > k or j < k:
        return 0
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    total = 0
    if i != k:
        total += last_chocolate(i + 1, j, k, memo)
    if j != k:
        total += last_chocolate(i, j - 1, k, memo)
    
    memo[(i, j)] = total
    return total

if __name__ == "__main__":
    n = 10
    dp = {}
    print(last_chocolate(1, 10, 4, dp))
