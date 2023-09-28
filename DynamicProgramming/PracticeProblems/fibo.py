def fibo_dp(n, arr):
    if n <= 1:
        return n
    
    if arr[n] != -1:
        return arr[n] # return if stored
    
    arr[n] = fibo_dp(n-1, arr) + fibo_dp(n-2, arr) # store in the arr
    return arr[n] # then return


def fibo_tabular(n):
    arr = [0, 1] + [-1]*(n-1)

    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n]


def fibo_const_space(n):
    second_last = 0
    last = 1

    for i in range(2, n+1):
        cur = second_last + last
        second_last = last
        last = cur

    return cur



if __name__ == "__main__":
    n = 120
    fib_list = [-1]*(n+1)
    print(fibo_dp(n, fib_list))
    print(fibo_tabular(n))
    print(fibo_const_space(n))