"""
Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được
một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím.
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
    for i in range(2, n):
        if check_prime(i):
            if check_prime(int(str(i)[::-1])):
                print(i)
                
solve(int(input()))