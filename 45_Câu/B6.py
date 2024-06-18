"""
Hai số tạo thành một cặp số thân thiết khi chúng tuân theo quy luật: Số này bằng tổng tất
cả các ước của số kia (trừ chính số đó) và ngược lại. Viết chương trình tìm hai số dạng này nhỏ
hơn N (với N nhập vào từ bàn phím).
"""

def tong_uoc(n):
    sum = 0
    for i in range(1, n // 2):
        if n % i == 0:
            sum += i
    return sum

def solve(n):
    for a in range(1, n):
        b = tong_uoc(a)
        if b < n and b != a:
            if tong_uoc(b) == a:
                print(a, b)
            
solve(int(input()))