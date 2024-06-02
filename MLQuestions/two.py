# Given 'n' integers, find their mean, median and mode.

# You are required to fill in a function that takes as inputs an integer' input1' (1) <= input1 <= 1000) and an integer array input2[], containing 'input1'
# integers, and returns output1 as the mean, output2 as the median and output3 as the mode. The mean and median must be correct to six decimal places.

# Mean:
# Defined as the average of all numbers in the array

# Median:
# Defined as the middle element of the array.

# If n is even, the median is the average of the two middle elements. If n is odd, the median is the middle element of the array

# Note: For finding the median, elements in the array have to be listed in numerical order from smallest to largest

# Mode:
# Defined as the number in the array with the highest frequency.
# If many numbers have the same highest frequency, then the mode is calculated by breaking ties in favour of the smallest of the numbers.

# Input Specification:
# input1: Integer in the range of 1 <= input1 <= 1000, denoting length of input array.
# input2: Integer input array

# Output Specification:
# Return output1 (double) variable as the mean Return output2 (double) variable as the median. Return output3 (int) variable as the mode.

# Example 1:
# input1: 3
# input2: {1,2,3}
# Output: 2.000000, 2.000000, 1

# Example 2:
# input1: 5
# input2: (41,18467,6334,26500,19169}
# Output: 14102.200000, 18467.000000, 41


def solve(n, arr):
    mean = sum(arr) / n
    sorted_arr = sorted(arr)
    median = float(sorted_arr[n // 2])

    if n % 2 == 0:
        median = (float(sorted_arr[n // 2]) + float(sorted_arr[n // 2 - 1])) / 2

    mode = max(arr, key=arr.count)

    return f"{mean:.6f}", f"{median:.6f}", mode


if __name__ == "__main__":
    n = 5
    arr = [41, 18467, 6334, 26500, 19169]
    print(solve(n, arr))
