def increment_count(d_map, arr, i, j):
    while i < j:
        if d_map.get(arr[i], 0):
            d_map[arr[i]] -= 1
        i += 1

def solve(arr: str, string: str) -> int:
    n = len(arr)
    k = len(string)
    ans = 0
    str_dict = {}
    for char in string:
        str_dict[char] = str_dict.get(char, 0) + 1

    # Main logic
    i, j = 0, 0

    while j < n:

        if str_dict.get(arr[j], 0) > 0:
            str_dict[arr[j]] -= 1
            if j == k + i - 1:
                ans += 1
                str_dict[arr[i]] += 1
                i +=1
        else:
            increment_count(str_dict, arr, i, j)
            i += 1

        j += 1
    return ans


if __name__ == "__main__":
    arr = "abcbacab"
    string = "abc"
    print(solve(arr, string))  

