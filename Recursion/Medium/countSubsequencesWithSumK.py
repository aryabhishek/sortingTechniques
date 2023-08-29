def solution(ind, total, k, arr):
    if ind == len(arr):
        if total == k:
            return 1
        
        return 0
    
    l = solution(ind+1, total + arr[ind], k, arr)
    r = solution(ind+1, total, k, arr)
    return l + r


if __name__ == "__main__":
    ar = [1,2,1]
    k = 2
    print(solution(0, 0, k, ar))