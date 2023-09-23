def my_solution(nums): # better than sorting, TC: O(2n), SC: O(1)
    zero = 0
    one = 0
    two = 0

    for num in nums:
        if num == 0:
            zero += 1
        
        elif num == 1:
            one += 1

        else:
            two += 1

    ind = 0
    for i in range(zero):
        nums[ind] = 0
        ind += 1

    for i in range(one):
        nums[ind] = 1
        ind += 1

    for i in range(two):
        nums[ind] = 2
        ind += 1


# Dutch National Flag Algorithm

def optimal(arr): # TC: O(n), SC:O(1)
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1

        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    

if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    optimal(arr)
    print(arr)