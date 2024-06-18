"""
Viết chương trình tính tổng của các số nguyên tố nhỏ hơn hoặc bằng N với N được nhập
từ bàn phím.
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
    sum = 0
    for i in range(2, n + 1):
        if check_prime(i):
            sum += i
            
    return sum

print(solve(int(input())))