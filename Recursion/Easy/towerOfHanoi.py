def solve(n, source, destination, helper):
    if n == 1:
        print(f"Disk {n} moved from {source} to {destination}")
        return

    solve(n-1, source, helper, destination)
    print(f"Disk {n} moved from {source} to {destination}")
    solve(n-1, helper, destination, source)


if __name__ == "__main__":
    n = 3
    solve(n, "Source", "Destination", "Helper")