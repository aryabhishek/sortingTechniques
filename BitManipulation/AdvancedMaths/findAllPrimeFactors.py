
from math import sqrt
from checkPrime import Solution


class NewSolution(Solution):
    def print_primes(self, N):
        # code here
        primes = []
        i = 2
        while i <= sqrt(N):
            if N % i == 0:
                primes.append(i)
            while N % i == 0:
                N //= i
            i += 1
        
        if N != 1:
            primes.append(N)
        
        return primes
    

if __name__ == "__main__":
    N = 7890
    print(NewSolution().print_primes(N))