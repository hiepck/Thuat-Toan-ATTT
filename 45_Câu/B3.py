"""
Cho một số nguyên dương N, gọi:
- k là số ước nguyên tố của N;
- q là tổng của các ước nguyên tố của N;
- p là tổng của các ước số của N;
- s là số ước của N;
Hãy viết chương trình tính giá trị của: N+p+s-q-k với N cho trước nhập từ bàn phím.
Ví dụ: N=24, có các ước là {1,2,3,4,6,8,12,24} do đó:
p=1+2+3+4+6+8+12+24=60 và s=8
trong đó có 2 ước nguyên tố là {2,3} do đó:
q=2+3=5 và k=2
Và từ đó: N+p+s-q-k = 24+60+8-5-2=85;
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
    uoc = [] #[+]
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    uoc_nguyen_to = [] #[+]
    for i in uoc:
        if check_prime(i):
            uoc_nguyen_to.append(i)
            
    k = len(uoc_nguyen_to) # k là số ước nguyên tố của N; 
    q = 0 # q là tổng của các ước nguyên tố của N;
    for i in uoc_nguyen_to:
        q += i
    p = 0 # p là tổng của các ước số của N;
    for i in uoc:
        p += i
    s = len(uoc) # s là số ước của N;
    print(uoc)
    print(uoc_nguyen_to)
    print(f"k = {k}, q = {q}, p = {p}, s = {s}")
    return n + p + s - q - k

print(solve(24))
    
    
    
