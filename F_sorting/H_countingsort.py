def method1(ll: list) -> list:
    def countSort(ll):
        output = [0 for i in range(256)]
        count = [0 for i in range(256)]
        ans = ["" for _ in ll]

        for i in ll:
            count[ord(i)] += 1

        for i in range(256):
            count[i] += count[i - 1]

        for i in range(len(ll)):
            output[count[ord(ll[i])] - 1] = ll[i]
            count[ord(ll[i])] -= 1

        for i in range(len(ll)):
            ans[i] = output[i]
        return ans

    return countSort(ll)


if __name__ == "__main__":
    
    l = ['1', '3', '4', '7', '5', '9']
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) 
    
