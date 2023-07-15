def brute_force(arr): # TC: O(n^2), SC: O(1)

    for num in arr:
        if arr.count(num) == 1:
            return num
        
def better(arr): # TC: O(n), SC: O(n)

    hash_map = {}

    for num in arr:
        hash_map[num] = hash_map.get(num,0) + 1

    for key, value in hash_map.items():
        if value == 1:
            return key


def optimal(arr): # TC: O(n), SC: O(1)
    ans = 0

    for num in arr:
        ans ^= num

    return ans
        

if __name__ == "__main__":
    arr = [1,1,2,3,3,4,4,5,5]
    print(optimal(arr))

