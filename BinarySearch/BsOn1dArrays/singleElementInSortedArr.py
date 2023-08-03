def find_single_element(nums):
    n = len(nums)

    if n == 1: return nums[0]

    elif nums[1] != nums[0]: return nums[0]

    elif nums[-2] != nums[-1]: return nums[-1]

    low = 1
    high = n - 2

    while low <= high:

        mid = (high - low)//2 + low

        if nums[mid-1] != nums[mid] != nums[mid+1]:
            return nums[mid]

        elif (mid%2 and nums[mid-1] == nums[mid]) or (not mid%2 and nums[mid+1] == nums[mid]):
            low = mid + 1

        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [1,1,2,3,3,4,4,8,8]
    print(find_single_element(arr))