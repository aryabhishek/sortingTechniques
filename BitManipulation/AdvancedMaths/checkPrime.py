from math import sqrt


class Solution:
    def is_prime(self, N):
        # code here
        count = 0
        for num in range(1, int(sqrt(N)) + 1):
            if N % num == 0:
                count += 1
                if N / num != num:
                    count += 1
            if count > 2:
                break
        
        return count == 2
    

if __name__ == "__main__":
    N = 2
    print(Solution().is_prime(N))