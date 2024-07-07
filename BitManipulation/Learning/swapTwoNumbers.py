if __name__ == "__main__":
    a = 5
    b = 7
    a = a ^ b
    b = a ^ b # b = a ^ b ^ b [b ^ b = 0] therefore b = a
    a = a ^ b # a = a ^ b ^ b [b = a] therefore a ^ a ^ b => a = b
    print(a, b)