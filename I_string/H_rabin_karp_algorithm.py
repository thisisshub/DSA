def method1(pat: str, txt: str, g: int) -> int:
    d = 256
    m = len(pat)
    n = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    for i in range(m - 1):
        h = (h * d) % g
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1
            if j == m:
                return "Pattern Found at index: " + str(i)

        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % g
            if t < 0:
                t += g


if __name__ == "__main__":
    """
    from timeit import timeit
    txt = "this is a string"
    pat = "this"
    g = 101
    print(timeit(lambda: method1(txt, pat, g), number=10000)) # 0.009983864998503122
    """
