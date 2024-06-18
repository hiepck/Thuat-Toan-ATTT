"""
Viết chương trình tìm số nguyên dương x nhỏ nhất và nhỏ hơn N nhập từ bàn phím sao
cho giá trị của biểu thức 𝐴𝑥2 + 𝐵𝑥 + 𝐶 là một số nguyên tố với A,B,C là các số nguyên nhập vào
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

def solve(A, B, C, N):
    for i in range(1, N):
        res = A * i * i + B * i + C
        if check_prime(res):
            return i

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
N = int(input("N = "))
print(solve(A, B, C, N))