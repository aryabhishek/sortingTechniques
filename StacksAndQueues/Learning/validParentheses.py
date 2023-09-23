def is_valid(s: str) -> bool:
    if len(s) < 2:
        return False

    stack = []

    for i in s:
        if i in '([{':
            stack.append(i)

        elif i in ")]}":
            if not stack:
                return False

            top = stack.pop()

            if i == ')' and top != '(':
                return False

            elif i == ']' and top != '[':
                return False

            elif i == '}' and top != '{':
                return False

    return False if stack else True


if __name__ == "__main__":
    s = "()[(]{}"

    print(is_valid(s))
