def method1(str1: str, str2: str) -> int:
    def compare(str1, str2):
        for i in range(256):
            if str1[i] != str2[i]:
                return False
        return True

    def search(pat, txt):
        m = len(pat)
        n = len(txt)

        count_p = [0] * 256
        count_t = [0] * 256

        for i in range(m):
            count_p[ord(pat[i])] += 1
            count_t[ord(txt[i])] += 1

        for i in range(m, n):
            if compare(count_p, count_t):
                return ("Found at ", i - m)
            
            count_t[ord(txt[i])] += 1
            count_t[ord(txt[i-m])] -= 1

        if compare(count_p, count_t):
            return ("Found at ", n - m)

    txt = "thisisastringtocompare"
    pat = "thisisiastring"

    search(pat, txt)


if __name__ == "__main__":
    """
    from timeit import timeit
    txt = "thisisastringtocompare"
    pat = "thisisiastring"
    print(timeit(lambda: method1(pat, txt), number=10000)) # 0.4546106020006846
    """
