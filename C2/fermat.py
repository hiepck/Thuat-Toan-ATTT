import random

def fermat(n, t):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for _ in range(t):
        rand = random.randint(2, n - 2)
        if (pow(rand, n - 1) % n) != 1:
            return False
        
    return True



if fermat(int(input()), 1):
    print("Co the la snt")
else:
    print("Khong phai la snt")
    
    