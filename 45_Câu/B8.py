"""
Một số gọi là số Т-prime nếu có có đúng 3 ước nguyên dương. Viết chương trình tìm các
số Т-prime nhỏ hơn hoặc bằng N với N cho trước nhập từ bàn phím.
"""

def solve(n):
    for i in range(1, n + 1):
        count = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            print(i)
            
solve(int(input()))