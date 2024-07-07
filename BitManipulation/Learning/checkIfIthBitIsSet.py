def check_using_right_shift(num: int, i: int) -> bool:
    return (num >> i) & 1

def check_using_left_shitf(num: int, i: int) -> bool:
    return num & (1 << i)


if __name__ == "__main__":
    print(check_using_right_shift(13, 2))
    print(check_using_left_shitf(13, 1))