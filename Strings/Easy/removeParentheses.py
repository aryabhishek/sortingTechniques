def remove_outer_parentheses(s: str) -> str:
    ans = ''

    equal = 0
    left = 0
    right = 0

    while right < len(s):
        if s[right] == "(":
            equal += 1

        elif s[right] == ")":
            equal -= 1

        if equal == 0:
            ans += s[left+1:right]
            left = right + 1

        right += 1

    return ans


if __name__ == "__main__":
    s = "(()())(())(()(()))"

    print(remove_outer_parentheses(s))
