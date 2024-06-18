"""
Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N với N nhập vào từ bàn
phím, sao cho tổng và hiệu của chúng đều là số nguyên tố.
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
    print
    for i in range(0, len(primes)):
        for j in range(i + 1, len(primes)):
            if check_prime(primes[i] + primes[j]) and check_prime(abs(primes[i] - primes[j])):
                print(primes[i], primes[j])

solve(int(input()))