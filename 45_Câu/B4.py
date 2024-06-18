"""
Viết chương trình đếm số số nguyên tố nằm trong khoảng [A,B] với A, B nhập vào từ bàn
phím.
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

def count_prime(A, B):
    count = 0
    for i in range(A, B + 1):
        if check_prime(i):
            count += 1
    return count

A = int(input())
B = int(input())
print(count_prime(A, B))
            