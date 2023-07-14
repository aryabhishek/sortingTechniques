def find_missing_num(arr): # from 0 to n
    n = len(arr)
    
    xor = 0

    for i in range(n):
        xor ^= arr[i] ^ (i+1)

    return xor


def find_missing_number(arr):
    n = len(arr) + 1

    actual_sum = n * (n+1) // 2

    arr_sum = sum(arr)

    return actual_sum - arr_sum

if __name__ == "__main__":
    arr = [0,2,3,4,5]
    print(find_missing_num(arr))