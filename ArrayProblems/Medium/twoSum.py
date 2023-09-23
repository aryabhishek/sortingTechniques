def twoSum(nums: list[int], target: int) -> list[int]:
        
        seen = {}

        for i, val in enumerate(nums):

            rem = target - val

            if rem in seen:
                return [i, seen[rem]]

            seen[val] = i


if __name__ == "__main__":
    arr = [2,7,11,15]
    target = 9

    print(twoSum(arr, target))