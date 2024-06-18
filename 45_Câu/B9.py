"""
Viết chương trình đếm số số nguyên tố nhỏ hơn hoặc bằng N với N được nhập vào từ bàn
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

def solve(n):
    count = 0
    for i in range(2, n + 1):
        if check_prime(i):
            count += 1
    return count

print(solve(int(input())))