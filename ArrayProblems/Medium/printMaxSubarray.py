def solution(arr):

    n = len(arr)

    ans = float("-inf")
    total = 0
    ans_start, ans_end = 0, 0

    for i in range(n):
        if total == 0:
            start = i
        total += arr[i]
        if total > ans:
            ans = total
            ans_start = start
            ans_end = i
        if total < 0:
            total = 0

    return ans, (ans_start, ans_end+1)

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum, max_subarray = solution(arr)
    print("Max sum:", max_sum)
    print("Max Subarray:", arr[max_subarray[0]:max_subarray[1]])