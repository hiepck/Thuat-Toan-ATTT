"""
Viết chương trình tìm bốn số nguyên tố liên tiếp, sao cho tổng của chúng là số nguyên tố
nhỏ hơn hoặc bằng N (với N được nhập vào từ bàn phím).
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

def sovle(n):
    primes = []
    for i in range(2, n + 1):
        if check_prime(i):
            primes.append(i)
            
    ket_qua = []
    index = 0
    res = 0
    while index + 4 <= len(primes):
        for i in range(0, 4):
            res += primes[index + i]
            ket_qua.append(primes[index + i])
            
        if check_prime(res) and res <= n:
            print(f"{ket_qua} = {res}")
            index += 1
            ket_qua = []
        else:
            index += 1
            ket_qua = []
    
    
    
sovle(int(input()))