def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr.pop()

    smaller, greater = [], []

    for item in arr:
        if item <= pivot:
            smaller.append(item)
        else:
            greater.append(item)

    return quick_sort_iterative(smaller) + [pivot] + quick_sort_iterative(greater)

def quick_sort_recursive(arr):
    pass


if __name__ == "__main__":
    lst = [5,4,3,2,1,69,-10,-2,11,3,3,2,9,-69]
    sorted_lst = quick_sort_iterative(lst)
    print(sorted_lst)