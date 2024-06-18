def phan_tich_snt(n):
    res = []
    p = 2
    while n > 1:
        if n % p == 0:
            res.append(p)
            n //= p
        else:
            p += 1
    return res

print(phan_tich_snt(int(input('Nhap n: '))))   