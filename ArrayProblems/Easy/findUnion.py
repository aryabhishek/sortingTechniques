def union(a: list, b: list) -> list:

    """Only sorted lists are accepted"""

    union = []

    i, j = 0, 0
    n, m = len(a), len(b)

    while i < n and j < m:

        if a[i] <= b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1

        else:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1

    while i < n:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    while j < m:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1

    return union


if __name__ == "__main__":
    a = [1,2,3,4,6]
    b = [2,3,5]
    print(union(a,b))