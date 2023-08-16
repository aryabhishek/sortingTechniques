def solve(n, source, destination, helper):
    if n == 1:
        # if there's only one disk just place it in source
        print(f"Disk {n} moved from {source} to {destination}")
        return

    # from source to helper with the help of destination
    solve(n-1, source, helper, destination)

    print(f"Disk {n} moved from {source} to {destination}")
    # from helper to destination with the help of source
    solve(n-1, helper, destination, source)


if __name__ == "__main__":
    n = 3
    solve(n, "Source", "Destination", "Helper")