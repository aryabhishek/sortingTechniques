class Solution:
    def shortestJobFirst(arr):
        arr.sort()
        time, wait_time = 0, 0

        for i in range(len(arr)):
            wait_time += time
            time += arr[i]

        return wait_time // len(arr)


if __name__ == "__main__":
    arr = [4, 3, 7, 1, 2]
    print(Solution.shortestJobFirst(arr))  # 4
