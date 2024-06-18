def sovle(t, p):
    index = -1
    for i in range(0, len(t)):
        if t[i] == p[0]:
            for j in range(0, len(p)):
                if t[i + j] != p[j]:
                    index = -1
                    break
                index = i
        if index != -1:
            break
    return index

t = 'a'*10 + 'h'
p = 'aaah'
print(sovle(t, p))
                