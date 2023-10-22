class TrieNode:
    def __init__(self):
        self.children = [None] * 2

    def contains_bit(self, bit) -> bool:
        return self.children[bit] != None

    def put(self, bit, node) -> None:
        self.children[bit] = node

    def get(self, bit):
        return self.children[bit]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num) -> None:
        cur = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not cur.contains_bit(bit):
                cur.put(bit, TrieNode())
            cur = cur.get(bit)

    def get_max_xor(self, num):
        cur = self.root
        maxi = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if cur.contains_bit(1 - bit):
                maxi = maxi | (1 << i)
                cur = cur.get(1 - bit)
            else:
                cur = cur.get(bit)

        return maxi


def maximumXor(A: list[int]) -> int:
    # write your code here
    trie = Trie()
    maxi = 0

    for num in A:
        trie.insert(num)

    for num in A:
        maxi = max(maxi, trie.get_max_xor(num))

    return maxi
