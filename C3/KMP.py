def KMP_search(text, pattern):
    # Tạo bảng tiền tố
    def compute_prefix_table(pattern):
        prefix_table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix_table[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix_table[i] = j
        return prefix_table

    # Tìm kiếm chuỗi con trong chuỗi mẹ
    prefix_table = compute_prefix_table(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = prefix_table[j-1]
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            print("Pattern found at index", i - j + 1)
            j = prefix_table[j-1]

# Ví dụ sử dụng
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMP_search(text, pattern)