def log(n: int, base: int) -> int:
    if n < base:
        return 0
    
    return log(n//base, base) + 1


if __name__ == "__main__":
    print(log(11,10))