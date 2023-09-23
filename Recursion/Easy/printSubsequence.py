def print_subseq(ind: int, empty: list) -> None:
    if ind >= n:
        print(empty)
        return
    
    empty.append(ar[ind])
    print_subseq(ind + 1, empty)
    empty.remove(ar[ind])
    print_subseq(ind + 1, empty)



if __name__ == "__main__":
    ar = [3,1,2]
    n = len(ar)

    print_subseq(0, [])