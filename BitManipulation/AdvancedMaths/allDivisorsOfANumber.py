from math import sqrt


class Solution:
    def print_divisors(self, N):
        # code here
        divisors = []
        for num in range(1, int(sqrt(N)) + 1):
            if N % num == 0:
                divisors.append(num)
                if N / num != num:
                    divisors.append(N // num)
        
        return divisors
    

if __name__ == "__main__":
    N = 24
    print(Solution().print_divisors(N))