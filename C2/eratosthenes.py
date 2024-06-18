import math

def simple_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n + 1, p):
                primes[i] = False
        p += 1
    
    isPrime = []
    for i in range(2, n + 1):
        if primes[i]:
            isPrime.append(i)
    return isPrime


def segmented_sieve(n):
    """Tìm tất cả các số nguyên tố từ 1 đến n bằng sàng Eratosthenes phân đoạn"""
    limit = int(math.sqrt(n)) + 1
    primes = simple_eratosthenes(limit)

    # Chia khoảng từ 0 đến n thành các đoạn
    low = limit + 1
    high = 2 * limit
    
    temp_primes =  []
    while low < n:
        if high >= n:
            high = n + 1
        
        mark = [True] * (high - low)
        
        for prime in primes:
            start = max(prime * prime, (low + prime - 1) // prime * prime)
            # print(f"prime = {prime}")
            # print(f"low = {low}")
            # print(f"(low + prime - 1) // prime * prime = {(low + prime - 1) // prime * prime}")
            for i in range(start, high, prime):
                mark[i - low] = False
        
        for i in range(low, high):
            if mark[i - low]:
                temp_primes.append(i)

        low += limit
        high += limit
    
    primes.extend(temp_primes)
    return primes
    
print(segmented_sieve(100))