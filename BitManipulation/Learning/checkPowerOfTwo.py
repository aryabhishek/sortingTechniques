def check_power_of_two(N: int) -> bool:
    return N & (N - 1) == 0


if __name__ == "__main__":
    print(check_power_of_two(2**10))
