def reverse_words(s: str) -> str:
    word_list = s.split()
    ans = ''
    for i in range(len(word_list)-1, -1, -1):
        ans += word_list[i] + " "

    return ans.rstrip()


if __name__ == "__main__":
    s = "the sky is blue"

    print(reverse_words(s))
