def method1(pat: str, txt: str) -> int:
    def kmp_search(pat, txt):
        m = len(pat)
        n = len(txt)

        lps = [0] * m
        j = 0

        compute_lps_array(pat, m, lps)
        i = 0
        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == m:
                return "Found pattern at: " + str(i - j)
                j = lps[j - 1]

            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def compute_lps_array(pat, m, lps):
        len = 0
        lps[0]
        i = 1

        while i < m:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1


if __name__ == "__main__":
    """
    from timeit import timeit
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    print(timeit(lambda: method1(pat, txt), number=10000)) # 0.001750715999150998
    """
