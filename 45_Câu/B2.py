"""
Viết chương trình tìm các số nguyên tố có N chữ số với N nhập từ bàn phím và 2 ≤ N ≤
10.
"""
import random
def fermat(n, t):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    for _ in range(t):
        rand = random.randint(2, n - 2)
        if (pow(rand, n - 1) % n) != 1:
            return False
    return True                                                                                            

def solve(n):
    # primes = []
    start = 10 ** (n - 1)
    end = 10 ** n - 1
    
    for i in range(start, end + 1):
        if fermat(i, 1):
            print(i, end=" ")
            

solve(int(input()))