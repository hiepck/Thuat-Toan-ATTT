"""
Viết chương trình tìm số nguyên tố có ba chữ số, biết rằng nếu viết số đó theo thứ tự
ngược lại thì ta được một số là lập phương của một số tự nhiên.
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



def solve():
    primes = []
    for i in range(100, 1000):
        if check_prime(i):
            primes.append(i)
    for i in range(0, len(primes)):
        str_prime = str(primes[i])
        re_prime = int(str_prime[::-1])
        if math.sqrt(re_prime) == int(math.sqrt(re_prime)):
            print(f"{primes[i]}: {re_prime} -> {int(math.sqrt(re_prime))}")
            
solve()