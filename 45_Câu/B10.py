"""
Viết chương trình đếm số ước và số ước nguyên tố của một số N nhập vào từ bàn phím.
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
    count_uoc = 0
    count_uoc_nguyen_to = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count_uoc += 1
            if check_prime(i):
                count_uoc_nguyen_to += 1
    print(count_uoc, count_uoc_nguyen_to)
    
solve(int(input()))