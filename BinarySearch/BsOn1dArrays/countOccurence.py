from findFirstAndLastOccurance import find_first_and_last_occurance

def my_solution(arr, k):
    ans = find_first_and_last_occurance(arr, k)

    if ans == [-1, -1]:
        return 0
    
    return ans[1] - ans[0] + 1

if __name__ == "__main__":
    nums = [1,1,1,2,2,3,3]
    target = 3

    print(my_solution(nums, target))