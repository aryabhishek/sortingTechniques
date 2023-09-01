def sum_digits(num: int, res: int) -> int:
    if num <= 0:
        return res
    
    return sum_digits(num//10, res + num%10)

if __name__ == "__main__":
    n = 12345
    print(sum_digits(n,0))
    
    