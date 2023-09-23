def insertion_sort(arr, n):
  for i in range(1, n):
    while arr[i-1] > arr[i] and i > 0:
      arr[i-1], arr[i] = arr[i], arr[i-1]
      i -= 1
