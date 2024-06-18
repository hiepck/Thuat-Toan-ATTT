"""
Viết chương trình tìm các số nguyên tố từ một mảng sinh ngẫu nhiên có kích thước N,
với N nhập vào từ bàn phím.
"""

import math
import random

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
    arr = []
    for i in range(0, n):
        randi = random.randint(0, 1000)
        arr.append(randi)
    
    print(arr)
    primes = []
    for i in range(0, len(arr)):
        if check_prime(arr[i]):
            primes.append(arr[i])
            
    return primes

print(solve(int(input())))