import math

p = 2147483647
m = math.ceil(math.log2(p)) 
W = 8 # so bit
t = math.ceil(m/W) # so phan tu

def tach_mang(a):
    #a = int(input('a = '))
    w = 8
    p = 2147483647
    m = math.ceil(math.log2(p))
    t = math.ceil(m/w)

    A = []
    for i in range(t-1, -1, -1):
        A.append((a//2**(i*w)))
        a = a % 2**(i*w)
    return A 

def tinh_mang(A):
    # A_string = input("Nhap mang: ")
    # A = [int(x) for x in A_string.split()]
    A = A[::-1]
    res = 0
    w = 8
    for i in range(0, len(A)):
        res += A[i] * 2**(i*w)
    return res

def cong(a, b):
    a = a[::-1] # doi lai chieu cua mang
    b = b[::-1]
    c = []
    epsilon = 0
    e = pow(2, W)
    for i in range(t):
        s = a[i] + b[i] + epsilon
        x = s % e
        if s > e:
            epsilon = 1
        else:
            epsilon = 0
        c.append(x)
    return [epsilon, c[::-1]]

def tru(a, b):
    a = a[::-1]
    b = b[::-1]
    c = []
    epsilon = 0
    e = pow(2, W)
    for i in range(t):
        s = a[i] - b[i] - epsilon
        x = s%e
        if s < 0:
            epsilon = 1
        else:
            epsilon = 0
        c.append(x)
    return [epsilon, c[::-1]]

def cong_Fp(a, b):
    epsilon, c = cong(a, b)
    tach_p = tach_mang(p)
    if epsilon == 1:
        temp, c = tru(c, tach_p)
    else:
        if tinh_mang(c) > p:
            temp, c = tru(c, tach_p)
    return [temp, c]
    
def tru_Fp(a, b):
    epsilon, c = tru(a, b)
    tach_p = tach_mang(p)
    if epsilon == 1:
        temp, c = cong(c, tach_p)
    return [temp, c]

def nhan(a, b):
    a = a[::-1]
    b = b[::-1]
    c = [0] * 8
    for i in range(0, 4):
        u = 0
        for j in range(0, 4):
            if i + j < 8:
                uv = c[i + j] + a[i]*b[j] + u
                u = uv >> 8
                v = uv & 0xFF # and voi 11111111
                c[i + j] = v
        if i + 4 < 8:
            c[i + 4] += u
    return c[::-1]

def nghich_dao(a, b):
    m, n = a, b
    xm, ym = 1, 0
    xn, yn = 0, 1
    
    while n != 0:
        q = m // n
        r = m % n
        xr, yr = xm - q * xn, ym - q * yn
        
        m, n = n, r
        xm, ym = xn, yn
        xn, yn = xr, yr
    return xm, ym


print(nghich_dao(11, 5))
