def largest_odd_number(num: str) -> str:
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2:
            return num[:i+1]

    return ''


if __name__ == "__main__":
    num = "52"

    print(largest_odd_number(num))
