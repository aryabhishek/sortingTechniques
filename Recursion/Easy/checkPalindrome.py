def check_palin(s: str) -> bool:
    if not s or len(s) == 1:
        return True

    if s[0] == s[-1]:
        op = s[1:-1]
        return check_palin(op)
    
    return False


def second_method(s: str, idx: int) -> bool:
    if idx >= len(s):
        return True
    
    if s[idx] != s[len(s)-idx-1]:
        return False
    
    return second_method(s, idx+1)


if __name__ == "__main__":
    string = 'naman'

    print(check_palin(string))
    print(second_method(string, 0))
