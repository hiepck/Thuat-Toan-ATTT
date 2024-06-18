"""
Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên tố hơn kém nhau 2 đơn vị.
Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc bằng N, với N được nhập vào từ bàn phím.
"""

import math
def check_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    primes = []
    for i in range(2, n + 1):
        if check_prime(i):
            primes.append(i)
    for i in range(0, len(primes)):
        for j in range(i + 1, len(primes)):
            if math.fabs(primes[i] - primes[j]) == 2:
                print(primes[i], primes[j])
                
solve(int(input()))