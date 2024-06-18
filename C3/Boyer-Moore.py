def bad_character_rule(pattern):
    bad_char_shift = {}
    for i in range(len(pattern)):
        bad_char_shift[pattern[i]] = i
    return bad_char_shift

def boyer_moore_search(text, pattern):
    bad_char_shift = bad_character_rule(pattern)
    print(bad_char_shift)
    m = len(pattern)
    n = len(text)
    s = 0  # s is shift of the pattern with respect to text

    while(s <= n-m):
        j = m-1

        while j >= 0 and pattern[j] == text[s+j]:
            j -= 1

        if j < 0:
            print("Pattern found at index", s)
            s += (m - bad_char_shift[text[s+m]] if s+m<n else 1)
        else:
            s += max(1, j - bad_char_shift.get(text[s+j], -1))

# Example usage
text = "ABAAABCD"
pattern = "ABC"
boyer_moore_search(text, pattern)