import random

def miller_rabin(n, t):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    s = 0
    d = n - 1
    
    while d % 2 == 0:
        d //= 2
        s += 1
        
    for _ in range(t):
        a = random.randint(2, n - 2)
        x = pow(a, d) % n
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2) % n
            if x == n - 1:
                break
        else:
            return False
    return True
