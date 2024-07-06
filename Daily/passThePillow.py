class NaiveSolution:
    def passThePillow(self, n: int, time: int) -> int:
        right = True
        pos = 1
        for i in range(1, time + 1):
            if right:
                pos += 1
            else:
                pos -= 1
            if i % (n - 1) == 0:
                right = not right
        return pos


class OptimalSolution:
    def passThePillow(self, n: int, time: int) -> int:
        right = (time // (n - 1)) % 2 == 0
        return (time % (n - 1) + 1) if right else (n - time % (n - 1))
