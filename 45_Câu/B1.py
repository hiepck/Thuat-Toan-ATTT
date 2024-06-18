"""
Một số gọi là Q-prime khi nó có đúng 4 ước số nguyên dương. Hãy viết chương trình in ra
các số Q-Prime nhỏ hơn hoặc bằng một số N cho trước nhập từ bàn phím.
"""

def solve(n):
    Q_primes = []
    for i in range(6, n):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 4:
            Q_primes.append(i)
            
    return Q_primes

print(solve(1000))