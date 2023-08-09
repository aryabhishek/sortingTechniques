def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:

        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    print(is_anagram(s, t))
