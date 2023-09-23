def number_of_nodes(level):
    return 2 ** (level-1)


if __name__ == "__main__":
    nodes = 7  # 1 based indexing

    print(number_of_nodes(nodes))
